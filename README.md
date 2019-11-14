# didYouGitIt
This repository contains code that is MIT licensed

## How to get started?
The lambda.py file can be copied into your own AWS lambda.

For the frontend of the standalone app, please host the files in the dist folder on S3.
Specify index.html
Replace the links to post to your own lambda API gateway (making sure to enable CORS)

You will also need to replace the redirect link in the lambda.py code (GET request).

Sample of standalone app here: http://didyougitit.s3-website-us-east-1.amazonaws.com/#/intro

And... you are good to go!