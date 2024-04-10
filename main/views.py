from django.shortcuts import render
from . import models
# Create your views here.
def portfolio(request):
    about_me = models.AboutMe.objects.last()
    education = models.Education.objects.all()
    skills = models.Skills.objects.all()
    expereiense = models.Expereiense.objects.all()
    profile = models.Profile.objects.all()
    partfolio = models.Partfolio.objects.all()
    contact = models.Contact.objects.all()
    
    context = {
        'about_me': about_me,
        'education': education,
        'skills': skills,
        'expereiense': expereiense,
        'profile': profile,
        'partfolio': partfolio,
        'contact': contact
    }


    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message') 
        models.Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )       
    return render(request, 'index.html', context)