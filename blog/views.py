from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.views import View


class HomeView(View):
    def get(self, request):
        States = State.objects.all()
        return render(request, 'blog/home.html',{'states': States})


class selfManagerView(View):
    def get(self, request, slug):
        States = State.objects.all()
        selfManager = SelfMgr.objects.get(slug=slug)
        posts = selfManager.user.author.all().order_by('-created_date')
        paginator = Paginator(posts, 4)  # 3 поста на каждой странице
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # Если страница не является целым числом, поставим первую страницу
            posts = paginator.page(1)
        except EmptyPage:
            # Если страница больше максимальной, доставить последнюю страницу результатов
            posts = paginator.page(paginator.num_pages)

        return render(request, 'blog/selfManager.html', {'posts': posts,'states': States})


class PostView(View):
    def get(self,request,slug):
        States = State.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/postView.html', {'post':post,'states': States})
