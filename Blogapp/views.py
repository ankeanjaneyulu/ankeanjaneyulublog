from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import EmailMessage,send_mail
from django.conf import settings
from .forms import MyForm
# Create your views here.
def HomePage(request):
    return render(request,'Home.html')
def AboutPage(request):
    return render(request,'About.html')
def ContactPage(request):
    return render(request,'Contact.html')
def MailPage(request):
    if request.method=='POST':
        form=MyForm(request.POST,request.FILES)
        if form.is_valid():
            Name=form.cleaned_data['Name']
            Subject=form.cleaned_data['Subject']
            Email=form.cleaned_data['Email']
            Message=form.cleaned_data['Message']
            send_mail('got mail from' + str(Email),
                      "name: " + str(Name) + "\n"
                      "email:" + str(Email) + "\n"
                      "subject: " + str(Subject) + "\n"
                      "message :" + str(Message),
                      settings.EMAIL_HOST_USER,
                      ['ankeanjineyulu@gmail.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/GoodBye')
    else:
        form=MyForm()
    return render(request,'Sendmail.html',{'form':form})
def GoodBye(request):
    return render(request,'Thanks.html')
