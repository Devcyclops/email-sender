import smtplib
import re
import sys

def welcome_screen():
    print(('Welcome to Email_Sender v1.0...').upper())
def mail():
    while True:
        print('Press 1 to exit or 2 to send emails')
        decision = input(": ")
        if decision == '2':
            print("Loading......")
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            email_to = input("Enter your email: ")
            email_from = input("Enter receiver\'s email: ")
            if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_to) and re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email_from):
                password = input("Enter your password: ")
                
                subject =  input("Enter email title/subject: ")
                body =  input("What\'s this email about?: ")

                try:
                    server.login(email_from, password)
                except smtplib.SMTPAuthenticationError:
                    print('Username or password is incorrect')
                msg = f"Subject: {subject}\n\n {body}"
                try:
                    print('\033[1;30;40m sending email.............. \n')
                    server.sendmail(
                        email_from,
                        email_to,
                        msg
                    )
                    server.quit()
                    print(f'\033[1;32;40m email sent to {email_to} succesfully \n')
                except smtplib.SMTPException:
                    print("\033[1;31;40m email not sent \n")
                
                else:
                    print('Enter a valid email address(es)')
                    email_to = input("Enter your email: ")
                    email_from = input("Enter receiver\'s email: ")
                    
            
            
        elif decision == '1':
            print("Exiting program........")
            sys.exit()
        else:
            print("Unrecognized input, Exiting program........")
            sys.exit()
            
            

            

if __name__ == '__main__':
    welcome_screen()
    mail()
        
        
