from django.shortcuts import render

# Create your views here.
from blog.models import Post



def home(request):
	context={
		'posts':Post.objects.all()
	}
	return render(request,"blog/home.html",context)

def about(request):
	return render(request,"blog/about.html")