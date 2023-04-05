from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid= os.getenv('account_sid')
auth_token =os.getenv('auth_token')
my_number=os.getenv('my_number')
twilio_number=os.getenv('twilio_number')

client= Client(account_sid, auth_token)

messageVoice= """
<Response>
<Say language="pt-BR">
Olá Usuario! Você está bem? Vou te passar as instruções necessárias para recuperar sua senha!
</Say>
</Response>
"""

call= client.calls.create(
                        twiml=messageVoice,
                        to=my_number,
                        from_=twilio_number
                    )