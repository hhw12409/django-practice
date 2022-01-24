from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag):
    # topics 전역변수 선언
    global topics
    li = ''
    for topic in topics:
        li += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {li}
        </ol>
        {articleTag}
        <ul>
            <li>
                <a href="/create/">create</a>
            </li>
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
    article = f'''
        <form action="/create/" method="POST"> 
            <p>
                <input type="text" name="title" placeholder="title">
            </p>
            <p>
                <textarea name="body" placeholder="body"></textarea>
            </p>
            <p>
                <input type="submit" value="제출">
            </p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))