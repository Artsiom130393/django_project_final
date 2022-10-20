from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('This is about page')

def home(request):
    return render(request, 'home.html',{'greeting':'Hello!', 'g':'Goodbye'})

def reverse (request):
    user_text = request.GET['usertext']
    len_words = len(user_text.split())
    reverse_user_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext':user_text,'rev':reverse_user_text,'kolic_slov':len_words},
                   )