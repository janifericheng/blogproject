import slug as slug
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    print(slug)
    posts = Post.object.all()
    return render('post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'posts': posts
    })

def about(request):
    return render(request, 'about.html', {})
