from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import AddPostForm
from django.views import generic


class BlogView(generic.ListView):
    template_name = 'testapp/Home.html'
    context_object_name = 'blogpost'

    def get_queryset(self):
        return Blog.objects.all()


class BlogDetail(generic.DeleteView):
    model = Blog
    template_name = 'testapp/BlogDetail.html'


def AddPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            author = request.user
            blog = Blog.objects.create(title = title, content = content, author = author, image = image) 
            blog.save()
            return HttpResponse('blog post create')

    else:
        form = AddPostForm()
        
        blog = Blog.objects.all()
    context = {'form':form}
    return render(request, 'testapp/additem.html', context)


def PostLike(request, postid):
    post = Blog.objects.get(id = postid)
    user = request.user
    if user.is_authenticated:

        if user in post.likes.all():
            return HttpResponse('you are like this post already')   
        post.likes.add(user)
        return redirect('detail', postid)
    else:
        return HttpResponse('you are not allow to like this post')


def PostUnLike(request, postid):
    post = Blog.objects.get(id = postid)
    user = request.user
    if user.is_authenticated:

        if user in post.likes.all():
            post.likes.remove(user)
            return redirect('detail', postid)
        else:
            return HttpResponse('you are not like this post')
    else:
        return HttpResponse('you are not allowto like this post')


    

# Create your views here.
# def BlogView(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#             blog = Blog.objects.create(title = title, content = content)
#             blog.save()
#             return HttpResponse('blog post create')

#     else:
#         form = AddPostForm()
        
#         blog = Blog.objects.all()
#     context = {'blogpost':blog, 'form':form}
#     return render(request, 'Home.html', context) 

# def BlogDetail(request, postid):
#     post = Blog.objects.get(id=postid)
#     context = {'post':post}    
#     return render(request, 'BlogDetail.html', context)
