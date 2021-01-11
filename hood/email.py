from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from smtplib import SMTPException

def send_welcome_email(username,email):
    # Creating message subject and sender
    subject = 'Welcome to Mtaani'
    sender = 'ignore.justtesting@gmail.com'

    #passing in the context vairables
    
    html_content = render_to_string('activation_account.html',{"username":username})
    text_content = "Hello {{username}}, Welcome to Mtaani! Mtaa means One's home area (neighborhood). Join your mtaa to be in the loop about everything happening in their neighborhood."
    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    
    try:
        msg.send()
    except SMTPException as e:
        print('There was an error sending an email, kindly check your email: ', e) 