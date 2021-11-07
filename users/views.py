from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        data = request.POST
        user_form = UserCreationForm(data)
        if user_form.is_valid():
            user_form.save()
            return redirect('tasks')
    register_form= UserCreationForm()
    context = {
        "form": register_form,
    }
    return render(request, 'users/registration/register.html', context)
