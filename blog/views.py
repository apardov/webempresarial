from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
def posts(request):
    # obtener los Post de la BD y enviar el context con la informacion
    posts = Post.objects.all()
    return render(request, template_name='blog/blog.html', context={'posts': posts})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, template_name='blog/category.html', context={'category': category})
