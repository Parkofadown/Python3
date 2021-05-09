import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'to email address'
email['subject'] = 'subject line'

email.set_content('email message')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # ensuring email secure
    smtp.starttls()
    # from email account
    smtp.login('enter gmail account, 'enter gmail password')
    # sends email message from above
    smtp.send_message(email)
    # lets you know it succeeded
    print('All good boss')
