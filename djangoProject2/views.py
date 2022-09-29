from django.shortcuts import render, redirect
from .forms import RegisterForm, ContactForm
from django.views.generic import ListView
from .models import Publisher
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model, login

User = get_user_model()

def contact_page(request):
    form = ContactForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            login(request, user)
            return redirect('home')
    context = {
        "form": form
    }
    return render(request, "contact/contact.html", context)
    # contact_form = ContactForm()
    # context = {
    #     'form': contact_form
    # }
    # if request.method == 'POST':
    #     print(request.POST.get('fullname'))
    # return render(request, "contact/contact.html", context)
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        newUser = User.objects.create_user(username, email, password)

    return render(request, "auth/register.html", context)


def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home_page.html')
    else:
        return redirect('contact')

class PublisherListView(ListView):
    queryset = Publisher.objects.all().values()
    template_name = 'auth/PublisherListView.html'

class UserListView(ListView):

    model = User
    template_name = 'contact/userlist.html'
# def PublisherListView(request):
#     query = Publisher.objects.all().values()
#     print(query)
#     context = {
#         'query': query
#     }
#     return render(request, "auth/PublisherListView.html", context)


