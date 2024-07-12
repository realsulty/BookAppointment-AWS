# Final Project brainstorming :brain: 
![image](pics/flexbook.drawio.png)

## Booking website Progress :
- Hosted a basic booking website in S3 bucket 
- Created a DynamoDB Tables to store booking details
- created a role with Permisions to : 
1. DynamoDB
2. Lambda Functions
- Created a Lambda Function to recive the code that will be trigger and insert the data to the DB
- Created a POST method API to send the data from the website 

### Current Issue : 
Upon Submiting the booked date a falied message appears on the screen 
![image](pics/screen1.png)

## TroubleShooting the issue :
- checking on the API endpoint with POSTMAN 

![image](pics/screen2.png)

the returned message comes back successful accepting a json body, this might means one thing which there might be a correction needed in the python code providedto lambda functions 

> No data is stored yet 



