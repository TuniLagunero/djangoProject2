from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    return render(request, "home_page.html")

def contact_page(request):
    contact_form = ContactForm()

    context = {
        'form': contact_form
    }
    if request.method == 'POST':
        print(request.POST.get('fullname'))
    return render(request, "contact/contact.html", context)