from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'},
]

def index(request):
    # topics 전역변수 선언
    global topics
    li = ''
    for topic in topics:
        li += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {li}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!' + id)