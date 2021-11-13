from django.shortcuts import redirect, render
from django.views.generic import View
from .models import Recruit, StoreList, User
from .forms import UserForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class IndexView(View):
    def get(self, request, *args, **kwags):
        slug = self.kwargs['slug']
        store_name = StoreList.objects.get(slug=slug)
        recruit_list = Recruit.objects.filter(store__name= store_name, publish=True)

        return render(request, 'app/index.html', {
            'recruit_list': recruit_list,
            'store_name': store_name,
            'slug':slug
            })
       
       
class DetailView(View):
    def get(self, request, *args, **kwags):
        recruit = Recruit.objects.get(pk=self.kwargs['pk'])

        form = UserForm()

        return render(request, 'app/detail.html', {
            'recruit': recruit,
            'form': form,
            'store_name': recruit.store
        })

    def post(self, request, *args, **kwags):
        form = UserForm(request.POST or None)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            user_age = form.cleaned_data.get('user_age')
            user_gender = form.cleaned_data.get('user_gender')
            user_email = form.cleaned_data.get('user_email')
            user_tel = form.cleaned_data.get('user_tel')

            form.save()
        if user_gender == '1':
            user_gender = '女性'
        else:
            user_gender = '男性'

        store = StoreList.objects.get(slug= self.kwargs['slug'])

        user = User.objects.order_by("id").last()
        user.user_store = store
        user.save()

        store_email = store.email

        recruit = Recruit.objects.get(pk=self.kwargs['pk'])

        context = { 
            'user_name': user_name ,
            'user_age': user_age ,
            'user_gender': user_gender ,
            'user_email': user_email ,
            'user_tel': user_tel ,
            'recruit': recruit,
            }

        subject = "応募を受け付けました"
        message = render_to_string('app/mails/mail.txt', context, request)
        from_email = settings.EMAIL_HOST  # 送信者
        recipient_list = [user_email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)

        subject = "新着応募がありました"
        message = render_to_string('app/mails/mail_admin.txt', context, request)
        from_email = settings.EMAIL_HOST # 送信者
        recipient_list = [store_email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)

        return redirect('thanks')

class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')