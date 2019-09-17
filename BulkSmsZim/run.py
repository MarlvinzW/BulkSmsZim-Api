from BulkSmsZim.text import send_message

username = ''
auth_token = ''
to = ['']
message = ''

response = send_message(username, auth_token, to, message)
print(response)


