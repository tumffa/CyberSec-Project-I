from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from convoapp.models import Post
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

@login_required
def homePageView(request):
    return render(request, 'index.html', {'yourusername': request.user.username, 'messages': get_posts()})

def registerView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('/login/')

@csrf_exempt
def postMessageView(request):
    if request.method == 'GET':
        message = request.GET.get('message')
        username = request.GET.get('username')
        query = "INSERT INTO Posts (username, text) VALUES ('" + username + "','" + message + "')"
        cursor = connection.cursor()
        cursor.executescript(query)
        return redirect('/')

# FIXED CODE
# @login_required
# def postMessageView(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         username = request.POST.get('username')
#         print((username, message))
#         Post.objects.create(username=username, text=message)
#         return redirect('/')
    

def get_posts():
    query = "SELECT username, text FROM Posts"
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return [{'username': row[0], 'text': row[1]} for row in rows]