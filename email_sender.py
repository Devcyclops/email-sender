import smtplib

def welcome_screen():
    print('Welcome to Email_Sender v1.0')

def mail(email_from, password, email_to, subject, body):
    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    try:
        server.login(email_from, password)
    except smtplib.SMTPAuthenticationError:
        print('Username or password is incorrect')
    subject = subject
    body = body
    msg = f"Subject: {subject}\n\n {body}"
    try:
        print('\033[1;30;40m sending email.............. \n')
        server.sendmail(
            email_from,
            email_to,
            msg
        )
        print(f'\033[1;32;40m email sent to {email_to} succesfully \n')
    except STMPException:
        print("\033[1;31;40m email not sent \n")
    
    server.quit()

if __name__ == '__main__':
    welcome_screen()
    while True:
        mail(
     input("Enter your email: "),
     input("Enter your password: "),
     input("Enter receiver email: "),
     input("Enter email title/subject: "),
     input("What\'s this email about?: ")
     )
        
