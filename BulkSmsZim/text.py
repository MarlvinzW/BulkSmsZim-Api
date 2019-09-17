import requests


def send_message(username, auth_token, to, message):

    if (username == '') or (auth_token == '') or (to == '') or (message == ''):
        response = 'Please Fill In All The Details'
        return response

    else:
        url = f'http://apis.bulksmszim.co.zw/texts.php?username={username}&salt={auth_token}&destinations={to}&message={message}'
        response = requests.post(url=url)
        return response.reason

