from random import randint
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
my_number = os.getenv("MY_NUMBER=+5511997689989")
twilio_number = os.getenv("TWILIO_NUMBER")

client = Client(account_sid, auth_token)

# import codigo randomico
otp = str(randint(1000, 9999))


call = client.calls.create(
    twiml=f'<Response><Say language="pt-BR">Olá Usuario! Você está bem? Vou te passar as instruções necessárias para recuperar sua senha!Insira o codigo a seguir: {otp}</Say></Response>',
    to=my_number,
    from_=twilio_number
)




