from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    context = {
        'title': 'NotMospol',
        'content': 'Notmospol- сайт по поддержке студентов'
    }

    return render(request,'main/index.html', context)

