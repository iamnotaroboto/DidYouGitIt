import axios from 'axios';

export interface TextAnswerRes {
  answer: string,
  isComplete: boolean,
  isCorrect: boolean,
  textFeedback: string
}


// eslint-disable-next-line import/prefer-default-export
export const getAnswer = async (questionId: string, userInput: string):
  Promise<TextAnswerRes> => {
  const url = 'https://epbusjjlfl.execute-api.us-east-1.amazonaws.com/default/didYouGitIt';
  const res = await axios.post(url, {
    ui: 'ui',
    input: userInput,
    hidden: questionId,
  });
  return res.data;
};
