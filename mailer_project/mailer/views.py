from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage


from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'mailer/base.html')

    def post(self, request):

        msg_to = request.POST.get('to', '')
        msg_subject = request.POST.get('subject', '')
        msg_message = request.POST.get('message', '')
        msg_attachment = request.FILES.get('file', '')
        message = 'mail sent succesfully'

        print(msg_attachment)

        if all([msg_to, msg_subject, msg_message]):
            try:
                email = EmailMessage(
                    subject=msg_subject,
                    body=msg_subject,
                    from_email=None,
                    to=[msg_to],
                    bcc=None,
                    reply_to=None,
                )
                if msg_attachment:
                    email.attach(msg_attachment.name, msg_attachment.read(), msg_attachment.content_type)

                email.send(fail_silently=False)
            except Exception as err:
                message = err
        else:
            message = 'mail not sent'

        return render(request, 'mailer/base.html', {'message': message})

