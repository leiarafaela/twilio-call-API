from secrets_1 import account_sid, auth_token, my_number, twilio_number
import os
from twilio.rest import Client


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