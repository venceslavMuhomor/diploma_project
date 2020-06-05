from datetime import timezone

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View

from blog.forms import PostForm
from blog.models import Post, State
from .forms import LoginForm
from django.contrib.auth.decorators import login_required



class dashboard(View):
    form = PostForm
    model = Post

    def get(self, request):
        States = State.objects.all()
        post = Post.objects.all()
        form = PostForm()
        return render(request,'account/dashboard.html',{'section':'dashboard', 'PostForm': form,'states': States})

    # def get(self,request, *args,**kwargs):
    #     States = State.objects.all()
    #     post = Post.objects.get(id=id)
    #     form=PostForm(instance=post)
    #     return render(request,'account/dashboard.html',{'section':'dashboard', 'PostForm': form,'states': States})

    
    def post(self, request):
        States = State.objects.all()
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/account')
        return render(request, 'account/dashboard.html', {'section': 'dashboard', 'PostForm': form,'states': States})

# class editPost(View):
#     def get(self,request,id):
#         States = State.objects.all()
#         post = Post.objects.get(id=id)
#         form=PostForm(instance=post)
#         return render(request,'account/post_edit.html',{'section':'dashboard', 'PostForm': form,'states': States})
#
#     def post(self,request):
#         States = State.objects.all()
#         form = self.form(request.POST, request.FILES)
#         if form.is_valid():
#             post=form.save(commit=False)
#             post.save()
#             return HttpResponseRedirect('/account')
#         return render(request, 'account/post_edit.html', {'section': 'dashboard', 'PostForm': form, 'states': States})

def editPost(request,pk):
    States = State.objects.all()
    post=get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account')
    else:
        form=PostForm(instance=post)
    return render(request, 'account/post_edit.html', {'section': 'dashboard', 'PostForm': form, 'states': States,'post':post})
