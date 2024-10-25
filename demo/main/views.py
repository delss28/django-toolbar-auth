from django.shortcuts import render

def index(reguest):
    return render(reguest,'main/index.html')
def about(reguest):
    return render(reguest,'main/pages/about.html')
def contact(reguest):
    return render(reguest,'main/pages/contact.html')
def vacancies(reguest):
    return render(reguest,'main/pages/vacancies.html')
# Create your views here.
