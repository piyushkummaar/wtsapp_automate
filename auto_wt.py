'''
    Automate What'sapp messages
'''
from twilio.rest import Client

account_sid = 'ACc5169b63bd60f9303a71b406a8aeb3fa'
auth_token = '7df352a6967d97bb41c6f79ca021f23f'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',  # ',
    body="Hello I'am testing....",
    to='whatsapp:+918219471865'
)

print(message.sid)
