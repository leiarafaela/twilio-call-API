from twilio.rest import Client
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
my_number = os.getenv("MY_NUMBER")
twilio_number = os.getenv("TWILIO_NUMBER") # Substitua pelo código informado pelo usuário
verification_sid = os.getenv("VALIDATION_SID") # Substitua pela SID da verificação gerada pela API



client = Client(account_sid, auth_token)

# SID da verificação gerada pela API

# Verificar o código OTP
verification_check = client.verify \
                             .services('sua_service_sid') \
                             .verification_checks \
                             .create(to=my_number, code='343903')

# Verificar se a verificação foi aprovada
if verification_check.status == 'approved':
    print('Código verificado com sucesso!')
else:
    print('Código incorreto ou expirado.')
