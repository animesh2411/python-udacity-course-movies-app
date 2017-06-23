from twilio.rest import TwilioRestClient

account_sid = "AC241defadfa6116105fce98e4e0b19139" # Your Account SID from www.twilio.com/console
auth_token  = "364da11d573550d3b3dc54039cdb0011"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello This is animax? animesh Gupta",
    to="+918604784630",    # Replace with your phone number
    from_="+14153229994") # Replace with your Twilio number

print(message.sid)
