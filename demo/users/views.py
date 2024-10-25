from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from django.core.mail import send_mail
from django.template.loader import render_to_string


from users.forms import ProfileForm, UserAppointmentForm, UserLoginForm, UserRegistrationForm
from users.models import Appointment


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance

            auth.login(request,user)

            subject = 'Успешная регистрация'
            message = render_to_string('email.html', {'username': user.username})
            send_mail(subject, message, 'deliss2008@mail.ru', [user.email])

            messages.success(request, f"{user.username}, Вы успешно зарегистрированны и вошли в аккаунт")

            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserRegistrationForm()


    context = {
        'form': form,
    }
    return render(request,'users/registration.html',context)

def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")
                
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserLoginForm()
    
    context = {
        'form': form,
    }
    return render(request,'users/login.html',context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлён")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    appointments = Appointment.objects.filter(id_user=request.user)

    context = {
        'form': form,
        'appointments': appointments,
    }
    return render(request,'users/profile.html',context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:home'))

@login_required
def appointment(request):
    if request.method == "POST":
        form = UserAppointmentForm(data=request.POST)
        if form.is_valid():
            appointment = form.save()
            appointment.save()
            print(request.POST) 

            messages.success(request, f"{request.user.username}, Вы успешно записались")
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserAppointmentForm()

    context = {'form': form}
    return render(request, 'users/appointment.html', context)
