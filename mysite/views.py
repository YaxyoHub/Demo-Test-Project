from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Email_OTP
from .forms import Register_Form
from django.contrib import messages

from blog.models import Post
from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='login')
def home_view(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }

    return render(
        request, 'index.html',
        context=data
    )

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        i_password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=i_password
        )
        if user == None:
            messages.error(request, 'Login yoki Password Xato!')
            return redirect(
                'login'
            )
        else:
            login(request, user=user)
            return redirect('home')

    else:
        return render(
            request, 'login.html'
        )

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')   

    if request.method == 'POST':
        form = Register_Form(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data["password"])
            user.is_active = False
            user.save()

            user_email = form.cleaned_data.get('email')
            request.session['user_email'] = user_email

            import random
            code = str(random.randint(100000, 999999))

            Email_OTP.objects.create(
                user=user,
                code=code,
                email=user_email
            )

            send_mail(
                subject='Tasdiqlash kodi!',
                message=f"Tasdiqlash kodingiz: {code}",
                from_email=None,
                recipient_list=[user_email]
            )
            messages.success(request, 'Emailingizga kod yuborildi!')

            return redirect('verify_email')
        else:
            messages.error(request, form.errors)
            return redirect('register')

    else:
        empty_form = Register_Form()
        return render(
            request,
            'register.html',
            context={'form': empty_form}
        )


def verify_email_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        user_email = request.session.get('user_email')
        original_code = Email_OTP.objects.filter(email=user_email).first()

        print(f"CODE: {code}")
        print(f"USER EMAIL: {user_email}")
        print(f"ORIGINAL CODE: {original_code.code}")

        if not original_code.code == code:
            messages.error(
                request,
                'Tasdiqlash kodi xato!'
            )
            return redirect('verify_email')
        elif original_code.muddati_otganmi:
            messages.error(
                request,
                'Kod eskirgan, iltimos qayta ro`yxatdan o`tib, yangisini oling'
            )
            User.objects.delete(email=user_email)
            return redirect('register')
        else:
            messages.success(
                request,
                'Emailingiz tasdiqlandi!'
            )

            user = User.objects.filter(email=user_email).first()
            user.is_active = True
            user.save()

            login(
                request,
                user
            )
            original_code.delete()
            return redirect(
                'home'
            )


    else:
        return render(
            request,
            'verify_email.html'
        )

from allauth.socialaccount.models import SocialAccount

def profile(request):
    social = SocialAccount.objects.filter(
        user=request.user, 
        provider='google'
    ).first()