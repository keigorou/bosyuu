from django import views
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, redirect, render
from django.views import generic
from django.views.generic import ListView, View
from django.views.generic.base import TemplateView
from .models import Recruit, StoreList
from .forms import UserForm
from app import models
from django.core.mail import send_mail
from django.template.loader import render_to_string


class IndexView(View):
    def get(self, request, *args, **kwags):
        slug = self.kwargs['slug']
        store_name = StoreList.objects.get(slug=slug)
        recruit_list = Recruit.objects.filter(store__name= store_name)

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
            'form': form
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
        store_email = store.email

        context = { 
            'user_name': user_name ,
            'user_age': user_age ,
            'user_gender': user_gender ,
            'user_email': user_email ,
            'user_tel': user_tel 
            }

        subject = "応募を受け付けました"
        message = render_to_string('app/mails/mail.txt', context, request)
        from_email = 'keigorou84@gmail.com'  # 送信者
        recipient_list = [user_email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)

        subject = "新着応募がありました"
        message = render_to_string('app/mails/mail_admin.txt', context, request)
        from_email = 'keigorou84@gmail.com'  # 送信者
        recipient_list = [store_email]  # 宛先リスト
        send_mail(subject, message, from_email, recipient_list)

        return redirect('thanks')

class ThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')