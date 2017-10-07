from twilio.rest import Client

#Your account sid and auth token from twilio.com/user/account
account_sid = "XXXXXXXXXXXXXXXXXXXX" #hidden the api credentials on GitHub as it is sensitive information.
auth_token = "XXXXXXXXXXXXXXXXXXXXXXX" #hidden the api credentials on GitHub as it is sensitive information.
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Twinkle please! Reduce some weight",
    to = "+91XXXXXXXXXX", #My actual phone number - hidden the sensitve information.
    from_ = "+1XXXXXXXX") #My twilio number - hidden the sensitve information.
print message.sid

