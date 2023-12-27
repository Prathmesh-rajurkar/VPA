import twilio
from twilio.rest import Client

account_sid = "ACb9187ae6038cebea182df7078ea8b80c"
auth_token = "7384288f0e3ed9d786e97a85c56a0d9e"
client = Client(account_sid, auth_token)

def sendMessage(msg):
    message = client.sendMessage(
        from_='whatsapp:+14155238886',
        body=msg,
        to='whatsapp:+917820892770'
    )

    print(message.sid)