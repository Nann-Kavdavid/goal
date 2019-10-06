from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from blog_app.forms import PostForm, CommentForm
from blog_app.models import Post, Comment
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.list import ListView

from django.shortcuts import redirect, render, get_object_or_404
# import pydevd
# pydevd.settrace('192.168.1.209', port=1234, stdoutToServer=True, stderrToServer=True)


def index(request, post_form=None, comment_form=None, username=''):
    post_form = post_form or PostForm()
    comment_form = comment_form or CommentForm()
    post = Post.objects.all().filter(author__exact=request.user)
    comments = Comment.objects.all()
    context = {'post_form': post_form,
               'comment_form': comment_form,
               'post_list': post,
               'comments_list': comments,
               }
    if username:
        user = get_object_or_404(User, username=username)
        post = Post.objects.all().filter(author__exact=user)
        context = {'post_form': post_form,
                   'comment_form': comment_form,
                   'post_list': post,
                   'comments_list': comments,
                   }
        return render(request, template_name='index.html', context=context)
    return render(request, template_name='index.html', context=context)


class UserPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('blog_app:index')

    def get_context_data(self, **kwargs):
        data = super(UserPostCreateView, self).get_context_data(**kwargs)
        data['post_list'] = Post.objects.all().filter(author__exact=self.request.user)
        return data

    def form_valid(self, form):
        if form.is_valid():
            form.instance.author = self.request.user  # set author to current user
            form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class UserCommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'index.html'

    def get_success_url(self):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return reverse('blog_app:index-user', kwargs={'username': post.get_author()})

    def get_context_data(self, **kwargs):
        data = super(UserCommentCreateView, self).get_context_data(**kwargs)
        data['comments_list'] = Comment.objects.all()
        return data

    def form_valid(self, form):
        if form.is_valid():
            form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
            form.instance.comments_by = self.request.user
            form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog_app:index')


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog_app:index')


class UserListView(ListView):
    model = User
    template_name = 'users.html'
