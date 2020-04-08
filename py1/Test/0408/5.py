# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC5b0bf95d261df25811e411e924eb76a8'
auth_token = '8bb9da004cf3a2c27edc76873e0c2377'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="오이이잉?",
         from_='+15593404974',
         to='+821045283260'
     )

print(message.sid)