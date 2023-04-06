from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid= os.getenv('account_sid')
auth_token =os.getenv('auth_token')
my_number=os.getenv('my_number')
twilio_number=os.getenv('twilio_number')
verify_sid=os.getenv('verify_sid')

client= Client(account_sid, auth_token)

otp_verification=client.verify.services(verify_sid).verifications.create(
    to=my_number, channel="call"
)  

print(otp_verification.status)
otp_code=input("Digite o código OTP aqui: ")

otp_vcheck=client.verify.services(verify_sid).verification_checks.create(
    to=my_number, code=otp_code
)
# Verificar se a verificação foi aprovada
if otp_vcheck.status == 'approved':
    print('Código verificado com sucesso!')
else:
    print('Código incorreto ou expirado.')

print(otp_vcheck)