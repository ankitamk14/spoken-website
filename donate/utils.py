from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import smtplib


def send_transaction_email(user_email, transaction_details):
    print("donate: Transaction Mail")
    # Render the email content using a template
    subject = 'Spoken Tutorial - School Donation Transaction Details'

    status = transaction_details['status']
    if status == 'S':
        transaction_details['status_msg'] = "Thank you. Your transaction has been successfully completed."
    else:
        transaction_details['status_msg'] = "We regret to inform you that your transaction could not be processed. Please try again or contact support."
    html_message = render_to_string('donate/transaction_email.html', {'transaction_details': transaction_details})
    plain_message = strip_tags(html_message)
    from_email = 'no-reply@spoken-tutorial.org'
    to = user_email
    try:
        print("donate: send mail")
        send_mail(subject, plain_message, from_email, [to], html_message)
        
    except BadHeaderError:
        print("donate: BadHeaderError")
        return False, "Invalid header found"
    except smtplib.SMTPAuthenticationError:
        print("donate: SMTPAuthenticationError")
        return False, "Authentication failed. Check your email credentials"
    except smtplib.SMTPRecipientsRefused:
        print("donate: SMTPRecipientsRefused")
        return False, "The recipient was refused by the server"
    except smtplib.SMTPSenderRefused:
        print("donate: SMTPSenderRefused")
        return False, "The sender address was refused by the server"
    except smtplib.SMTPDataError:
        print("donate: SMTPDataError")
        return False, "The server returned an unexpected error code"
    except smtplib.SMTPConnectError:
        print("donate: SMTPConnectError")
        return False, "Failed to connect to the email server"
    except Exception as e:
        print("donate: mail exception")
        print(str(e))
        return False, str(e)
    print("donate: mail sent successfully")
    return True, "success"
