from django.shortcuts import render
from django.http import Http404
from django.utils import timezone 
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:5]
	return render(request, 'blog/index.html', {'posts': posts})

def detail(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404('Post does not exist')
	return render(request, 'blog/post.html', {'post': post})

def posts(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/todos_posts.html', {'posts': posts})
