from twilio.rest import Client

TWILIO_SID = "AC6b271361dcc327aea75cfc9c168f4eee"
TWILIO_AUTH_TOKEN = "474e23f5182bbbf8f6d899424f5d97a0"
TWILIO_VIRTUAL_NUMBER = "+13168006176"
TWILIO_VERIFIED_NUMBER = "+17169037801"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
