This is a helper library for sending sms's via the BulkSmsZim Api (www.bulksmszim.co.zw)

USAGE :

1.First assign variables for  the authentication token, username , to and message ie 

 
username = 'Your Username'
auth_token = 'Your API Key'
to = ['263xxx', '263xxx]
message = 'Your Message'

and initialise them with their respective details as supplied from the bulk sms api dashboard ie auth_token(API KEY) and username

2.Set the message variable to the required message you want

3.The to variable is a list so it must be initialised like this:
to = ['263...', '263...']

4.Finally import the send_message function passing the four (username, auth_token,to and message) variables to the send_message variable and call it assigning it to a variable so as to get a response to send the message ie
from BulkSmsZim.main import send_message

response = send_message(username, auth_token, to, message)

5.If message was sent successfully, 'OK' should be the response

FULL USAGE EXAMPLE :

from BulkSmsZim.main import send_message

username = 'Your Username'
auth_token = 'Your API Key'
to = ['263xxx', '263xxx]
message = 'Your Message'


response = send_message(username, auth_token, to, message)
print(response)


