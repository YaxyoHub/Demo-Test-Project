from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import Post_Form, Edit_Post_Form
from django.contrib import messages

from django.core.mail import send_mail

# Create your views here.

@login_required(login_url='login')
def my_posts_view(request):
    user = request.user
    posts = Post.objects.filter(owner=user)
    data = {
        'posts': posts
    }
    return render(
        request,
        'my_posts.html',
        context=data
    )

@login_required(login_url='login')
def create_post_view(request):
    if request.method == 'POST':
        form = Post_Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            messages.success(
                request,
                'Post Yaratildi!'
            )
            return redirect(
                'my_posts'
            )
        else:
            messages.error(
                            request,
                            form.errors
                        )
            return redirect(
                'create_post'
            )

    else:
        empty_form = Post_Form()
        return render(
            request,
            'create_post.html',
            context={'form': empty_form}
        )

@login_required(login_url='login')
def edit_post_view(request, pk):
    select_post = Post.objects.get(pk=pk)
    if not select_post:
        messages.error(request, 'Bunday ID li post mavjud emas!')
        return redirect(
            'my_posts'
        )

    if request.method == 'POST':
        new_form = Edit_Post_Form(
            request.POST, 
            request.FILES, 
            instance=select_post
        )
        if new_form.is_valid():
            new_form.save()
            messages.success(
                request,
                'Post tahrirlandi!'
            )
            return redirect(
                'my_posts'
            )
        else:
            messages.error(
                request,
                new_form.errors
            )
            return redirect(
                'edit_post'
            )

    else:
        form = Edit_Post_Form(instance=select_post)
        return render(
            request,
            'edit_post.html',
            context={'form': form}
        )

@login_required(login_url='login')
def delete_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    messages.success(
        request,
        'Post o`chirildi!'
    )
    return redirect(
        'my_posts'
    )

@login_required(login_url='login')
def send_email_view(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        user_message = request.POST.get('message')

        send_mail(
            subject='Bu Xabar',
            message=user_message,
            from_email=None,
            recipient_list=[user_email]
        )
        messages.success(
            request,
            'Emailga xabar yuborildi'
        )
        return redirect('home')

    else:
        return render(
            request,
            'send-email.html'
        )
