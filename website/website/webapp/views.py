from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView
from webapp.forms import RegistrationForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def main(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['firstname'])
            print(form.cleaned_data['lastname'])
            print(form.cleaned_data['mobileno'])
            print(form.cleaned_data['city'])
            print(form.cleaned_data['pincode'])
            print(form.cleaned_data['address'])
    my_dict = {'form': form}
    return render(request, "contact.html", my_dict)


