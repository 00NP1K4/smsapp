from twilio.rest import Client

def sendsms(message, receiver):
    account_sid = 'ACdae8e3a59fd42bbf18e77a69e6cafb9b'
    auth_token = '49ef1ea9e7298e81232a58e0fd302488'

    client = Client(account_sid, auth_token)

    message = client.messages.create(body=message, from_='+12546137735', to=receiver)

    return message.sid