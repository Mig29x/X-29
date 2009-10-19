from django.core.mail import send_mail
import settings # Assumed to be in the same directory.
send_mail('Subject here', 'Here is the message.', 'from@example.com', ['miguel.barrera@gmail.com'], fail_silently=False)
