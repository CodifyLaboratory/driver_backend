from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.forms import UserForm
from user.personal_info.forms import PersonalInfoForm
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect("index")
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})
    else:
        return render(request, 'login.html', {"error": "Invalid action"})
        
def logout(request):
    django_logout(request)
    return redirect("index")

def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    elif request.method == 'POST':
        user_data = UserForm(request.POST)
        personal_info_data = PersonalInfoForm(request.POST)
        if user_data.is_valid() and personal_info_data.is_valid():
            personal_info_instance = personal_info_data.save()
            user_instance = user_data.save(False)
            user_instance.personal_info = personal_info_instance
            user_instance.set_password(user_data.cleaned_data['password'])
            user_instance.save()
            print('user_data is valid and saved')

        # save data, store token and redirect to main page
        return redirect("index")

