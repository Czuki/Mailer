from django.shortcuts import render
from django.core.mail import send_mail


from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'mailer/base.html')

    def post(self, request):

        msg_from = None
        msg_to = request.POST.get('to', '')
        msg_subject = request.POST.get('subject', '')
        msg_message = request.POST.get('message', '')

        message = 'mail sent succesfully'

        if all([msg_to, msg_subject, msg_message]):
            try:
                send_mail(
                    msg_subject,
                    msg_message,
                    msg_from,
                    [msg_to],
                    fail_silently=False,
                )
            except Exception as err:
                message = err
        else:
            message = 'mail not sent'

        return render(request, 'mailer/base.html', {'message': message})

