import json

import requests
from django.shortcuts import render

from .models import Contact


def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        #r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        r = requests.get('https://api.chucknorris.io/jokes/random?name=' + firstname + ' ' + lastname + '&category=dev')
        json_data = json.loads(r.text)
        joke = json_data.get('value')#.get('joke')

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)
    else:
        firstname = 'Shivam'
        lastname = 'Raj'
        #r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        r = requests.get('https://api.chucknorris.io/jokes/random?name=' + firstname + ' ' + lastname + '&category=dev')
        json_data = json.loads(r.text)
        joke = json_data.get('value')#.get('joke')

        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    r1=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text&text=?")
    q=r1.text
    context={'quote':q}
    return render(request, 'mysite/portfolio.html',context)


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')
