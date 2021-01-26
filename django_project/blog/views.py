from django.shortcuts import render

# Create your views here.


posts=[
	{
		'author':'Arjit Biswal',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted':'August 27,2018',

	},
	{
		'author':'Suresh',
		'title':'Blog Post 2',
		'content':'Second Post content',
		'date_posted':'August 28,2018',
	}
]

def home(request):
	context={
		'posts':posts
	}
	return render(request,"blog/home.html",context)

def about(request):
	return render(request,"blog/about.html")