from twilio.rest import Client

#Your account sid and auth token from twilio.com/user/account
account_sid = "AC50eee6c110e44e49d73723313daef507"
auth_token = "afeff4ce36757748c7cf7db56f729f7b"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Twinkle please! Reduce some weight",
    to = "+919819166570", #My actual phone number
    from_ = "+19544487442") #My twilio number
print message.sid

