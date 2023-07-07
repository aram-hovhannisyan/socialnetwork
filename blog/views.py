from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from django.urls import reverse_lazy, reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from blog.forms import CommentForm

# from django.http import HttpResponseRedirect



def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('blog-home')
    # return HttpResponseRedirect(reverse('blog-home', args=[str(pk)]))


def PostLikers(request, pk):
    # post = get_object_or_404(Post, id=request.POST.get('post_id'))
    for i in Post.objects.all():
        if i.id == pk:
            post = i
    # post = Post.objects.all()[request.POST.get('post_id')]
    context = {
        'post_likers': post.get_post_likers()
    }
    print(post.get_post_likers())
    return render(request, 'blog/post_likers.html', context=context)




def home(request):
    context = {
        'posts': Post.objects.all(),
        'total_likes': Post.total_likes(),
        'likers': Post.get_post_likers(),
        'liked': False
    }

    
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5






class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class AddCommentView(CreateView):

    model = Comment
    template_name = 'blog/add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)