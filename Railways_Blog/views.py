from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.
def post_list(request):
	#filtering posts in sorted order of published date
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#posts is used by post_list.html
	return render(request, 'Railways_Blog/post_list.html',{'posts':posts})