from django.shortcuts import render
# from django.http import HttpResponse 

posts = [
    {
        'author': 'Qwek',
        'title': 'Post 1',
        'content': 'Helloworld!',
        'date_posted': '25 April 2019'
    },
    {
        'author': 'Zhi Hui',
        'title': 'Post 2',
        'content': '2nd post',
        'date_posted': '25 April 2019'
    }
]

def home(request): 
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context) # render returns http
    
def about(request): 
    return render(request, 'blog/about.html', {'title' : 'About'}) # render returns http



#  HTTPRESONSE EXAMPLE
#  def about(request): 
#     return HttpResponse('<h1>Blog About</h1>')
