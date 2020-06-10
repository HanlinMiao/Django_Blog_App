from django.shortcuts import render

posts =[
    {
    'author' : 'Hanlin Miao',
    'title': 'Blog Post 1',
    'content': 'First Post content',
    'date_posted': '6/9/2020'
    },
    {
    'author' : 'Jane Doe',
    'title': 'Blog Post 2',
    'content': 'second Post content',
    'date_posted': '6/10/2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog_1/home.html', context)


def about(request):
    return render(request, 'blog_1/about.html', {'title': 'About'})

