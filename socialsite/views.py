from django.shortcuts import render
from .models import Post

posts = [ 
	{
		'author': 'Vishisht',
		'title': 'socialsite post 1',
		'content': 'First post content',
		'date':'Jan 18',
	},
	{
		'author': 'Yogesh',
		'title': 'socialsite post 2',
		'content': 'First post content',
		'date': 'Jan 28',
	}
]

def home(request):
	context = {
			'posts': Post.objects.all()
	}
	return render(request, 'socialsite/home.html', context)

def about(request):
	return render(request, 'socialsite/about.html', {'title': 'About'})

def profile(request):
	return render(request, 'socialsite/profile.html',{'title': 'Profile'})

