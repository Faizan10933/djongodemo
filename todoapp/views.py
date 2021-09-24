#from todoapp.models import Todo
from django.http import request, response
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Todo

def ind(request):
    myposts= Todo.objects.all()
    print(myposts)
    return render(request, 'todo.html', {'myposts': myposts})

def work(request, id):
    post = Todo.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'index.html',{'post':post})
   # return render(request, 'index.html')


'''
def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html',
                  {'post':post})

# Create your views here.
'''