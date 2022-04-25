from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january" : "Work Hard! in january.",
    "february" : "Work Hard! in february.",
    "march" : "Your Birthday! Lets celebrate.",
    "april" : "Work Hard! in april.",
    "may" : "Work Hard! in may.",
    "june" : "Work Hard! in june.",
    "july" : "Work Hard! in july.",
    "august" : "Work Hard! in august.",
    "september" : "Work Hard! in september.",
    "october" : "Work Hard! in october.",
    "november" : "Work Hard! in november.",
    "december" : None,
}

def home(request):
    months = list(monthly_challenges.keys())
    for i in range(len(months)):
        months[i]=months[i].capitalize()
    return render(request, 'challenges/index.html',{
        'months_list' : months
    })

def index_num(request,month):
    months = list(monthly_challenges.keys())

    if month<=len(months) and month>=1:
        return redirect('index-page', month=months[month-1])
    else:
        response_data = render_to_string('challenges/404.html')
        return HttpResponseNotFound(response_data)

def index(request,month):
    
    months = list(monthly_challenges.keys())
    if month not in months and month.lower() not in months:
        response_data = render_to_string('challenges/404.html')
        return HttpResponseNotFound(response_data)

    challenge_text = monthly_challenges.get(month)
    if challenge_text == None:
        challenge_text = monthly_challenges.get(month.lower())

    return render(request, 'challenges/challenge.html', {
            'month' : month,
            'text' : challenge_text
        })


