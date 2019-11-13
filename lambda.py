import json
def lambda_handler(event, context):
    method = event.get('httpMethod', {})
    # get method for returning UI
    if method == 'GET':
        redirect = 'http://didyougitit.s3-website-us-east-1.amazonaws.com/'
        return {
            "isBase64Encoded": False,
            "statusCode": 302,
            "headers": { "location": redirect }
        }
    if method == 'POST':
        postReq = json.loads(event.get('body', {}))
        
        if postReq:
            if "ui" in postReq:
                if "hidden" in postReq and "input" in postReq:
                    # Retrieve contents from the request
                    editable = postReq["input"].strip() # user code
                    hidden =  postReq["hidden"].strip() # hidden code
                    
                    isComplete, isCorrect, answer, message = checkCorrectness(hidden, editable)
                    
                    result = {
                        "statusCode": 200,
                        "headers": {
                            "Access-Control-Allow-Origin" : "*",
                            "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                            "Access-Control-Allow-Headers": "Content-Type",
                            "Content-Type": "application/json",
                        },
                        "body":  json.dumps({
                            "isComplete": isComplete,
                            "isCorrect": isCorrect,
                            "answer": answer,
                            "textFeedback": message
                        })
                    }
                    return result
            elif  "hidden" in postReq and "0" in postReq["hidden"] and "editable" in postReq and "0" in postReq["editable"]:
                # Retrieve the contents from the request
                editable = postReq["editable"]["0"].strip() # user code
                hidden =  postReq["hidden"]["0"].strip() # hidden code
                
                isComplete, isCorrect, answer, message = checkCorrectness(hidden, editable)
                
                allFeedback = {
                    "isComplete": isComplete,
                    "jsonFeedback": { "feedback": message },
                    "htmlFeedback": "<div>" + message + "</div>",
                    "textFeedback": message
                }
                        
                result = {
                    "statusCode": 200,
                    "headers": {
                        "Access-Control-Allow-Origin" : "*",
                        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                        "Access-Control-Allow-Headers": "Content-Type",
                        "Content-Type": "application/json",
                    },
                    "body":  json.dumps({
                        "isComplete": allFeedback["isComplete"],
                        "jsonFeedback": allFeedback["jsonFeedback"],
                        "htmlFeedback": allFeedback["htmlFeedback"],
                        "textFeedback": allFeedback["textFeedback"]
                    })
                }
                return result
                
        result = {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Origin" : "*",
                    "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Content-Type": "application/json",
                },
                "body":  json.dumps({
                    "error": "Bad request"
                })
            }
        return result
        
    result = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
                "Content-Type": "application/json",
            },
            "body":  json.dumps({
                "test": method
            })
        }
    return result

def checkCorrectness(hidden, editable):
    if hidden is None or hidden == "":
        message = "Something went wrong"
        return False, False, "", message
    if editable is None or editable == "":
        message = "Empty response, please try again"
        return False, False, "", message
    
    lowerCaseEditable = editable.lower()
    if hidden == "intro":
        ans = "done"
        if lowerCaseEditable == ans:
            return True, True, ans, "Let's get started!"
        else:
            return False, False, ans, "Input should be Done"
    if hidden == "question1":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 3)
        ans = "c"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly. Remote repository is not hosted on your local machine, and you need network connection to fetch data from Git Central Repository."
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "question2":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 3)
        ans = "c"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly. When you run git status, you can see staged files (currently in your index), modified and unstaged files, and untracked files."
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "question3":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 4)
        ans = "b"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly. When using git reset --hard HEAD~1 you will lose all uncommitted changes in addition to the changes introduced in the last commit. The changes won't stay in your working tree so doing a git status command will tell you that you don't have any changes in your repository."
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "question4":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 3)
        ans = "c"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly. Pushing has the potential to overwrite changes, caution should be taken when pushing."
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "question5":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 4)
        ans = "b"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, 'You have answered correctly. git branch -m “branchNewName”'
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "scenario1":
        ans = "acc"
        isValidEditable, feedback = isValidMultipleOption(lowerCaseEditable, 3)
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly"
            else:
                matchFeedback = matchOptionStringsToAnswer(lowerCaseEditable, ans)
                if matchFeedback != "":
                    return True, False, ans, matchFeedback
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "scenario2":
        ans = "caa"
        isValidEditable, feedback = isValidMultipleOption(lowerCaseEditable, 3)
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly"
            else:
                matchFeedback = matchOptionStringsToAnswer(lowerCaseEditable, ans)
                if matchFeedback != "":
                    return True, False, ans, matchFeedback
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "scenario3":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 3)
        ans = "b"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly"
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "scenario4":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 3)
        ans = "a"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly"
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback
    if hidden == "scenario5":
        isValidEditable, feedback = isValidOption(lowerCaseEditable, 3)
        ans = "b"
        if (isValidEditable):
            if lowerCaseEditable == ans:
                return True, True, ans, "You have answered correctly"
            return True, False, ans, "You have answered incorrectly, try again"
        else:
            return False, False, ans, feedback

def isValidOption(option, number):
    if number == 3:
        if option != "a" and option != "b" and option != "c":
            return False, "Input should be A, B, or C"
        else:
            return True, ""
    elif number == 4:
        if option != "a" and option != "b" and option != "c" and option != "d":
            return False, "Input should be A, B, C or D"
        else:
            return True, ""
    else:
        return False, "Something went wrong"
            
def isValidMultipleOption(option, noOfQns):
    if noOfQns == 3:
        if len(option) == noOfQns:
            for elem in option:
                isValidEditable, feedback = isValidOption(elem, 3)
                if isValidEditable == False:
                    return False, "Input should be one of the following: AAA, ABC, BCA, etc..."
            return True, ""
        else:
            return False, "You should provide give 3 answers like one of the following: AAA, ABC, BCA, etc..."
    else:
        return False, "Something went wrong"
        
def matchOptionStringsToAnswer(option, answer):
    message = ""
    if option[0] == answer[0]:
        message += "The first answer is correct. "
    if option[1] == answer[1]:
        message += "The second answer is correct. "
    if option[2] == answer[2]:
        message += "The third answer is correct. "
    return message.strip()