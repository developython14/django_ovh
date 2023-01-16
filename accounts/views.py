from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm  ,UserCreationForm,UserChangeForm
from .forms import CustomUserCreationForm,basecreate
from django.core.mail import send_mail
from django.template.loader import render_to_string
from twilio.rest import Client
from .models import Person
from .models import Organismes
from .models import Countries
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags


# Create your views here.
@login_required
def dash(request):
    return render(request, 'test.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            print('data valid')
            print(request.POST)
            user = form.get_user()
            login(request, user)
            return redirect('dash')
    return render(request, 'login.html' , {'form':AuthenticationForm})



def logoutview(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        user = User.objects.create_user(username=username , email = email ,first_name = first_name ,last_name =last_name )
        user.set_password(password)
        user.save()
        phone = request.POST['phone']
        emploi = request.POST['emploi']
        country_name = request.POST['country_name']
        organisme_name = request.POST['organisme_name']
        organisme_website = request.POST['organisme_website']
        organisme_adresse = request.POST['organisme_adresse']
        country = Countries(name = country_name)
        country.save()
        org = Organismes(name = organisme_name , website =organisme_website , adresse = organisme_adresse )
        accept_contrat = True
        org.save()
        person = Person(user = user , phone = phone , emploi = emploi,country = country,organisme = org ,accept_contrat =accept_contrat )
        person.save()
        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('email_confirm.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })
        send_mail(
        mail_subject,
        'Here is the message. salam mustapha from django',
        'from@example.com',
        [email],
        html_message = message,
        fail_silently=False,
        )   
    return render(request, 'signup.html' , {'form':CustomUserCreationForm ,'form1':basecreate})

def test(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        user = User.objects.create_user(username=username , email = email ,first_name = first_name ,last_name =last_name )
        user.set_password(password)
        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('email_confirm.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })
        plain_message = strip_tags(message)
        message = EmailMessage(mail_subject,plain_message, message, 'khasa@gmail.com', [email])
        message.content_subtype = 'html' # this is required because there is no plain text email message
        message.send()  
        university = request.POST['university']
        person = Person(user = user , university = university)
        person.save()
        print('succes')
    return render(request, 'test.html' , {'form':CustomUserCreationForm ,'form1':basecreate})




def main_view(request):
    context = {}
    return render(request, 'room.html', context=context)

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return HttpResponse('Activation link is invalid!')  