from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, Comment
from django.views.generic import ListView, CreateView, DetailView
from .forms import CreatePost, CreateComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


def ShowForumPage(request):
    data = {
        'title': 'Форум',

    }
    return render(request, 'forum/forum.html', data)


class ForumPage(ListView):
    model = Post
    template_name = 'forum/forum.html'
    context_object_name = 'Post'
    ordering = ['-date']
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            object_list = self.model.objects.filter(title=query)
        else:
            object_list = self.model.objects.all().order_by('-date')
        return object_list

    def get_context_data(self, **kwargs):
        ctx = super(ForumPage, self).get_context_data(**kwargs)
        ctx['title'] = 'Форум'
        return ctx


def single_post(request, pk):
    form = ""
    this_post = Post.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateComment(request.POST, instance=request.user)
            if form.is_valid():
                Comment.objects.create(for_this=this_post, author=request.user, text=form['text'].value())
                form.save()
                messages.success(request, 'done')
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            form = CreateComment()
    data = {
        'post': this_post,
        'title': Post.objects.filter(id=pk).first(),
        'form': form,
        'Comment': Comment.objects.filter(for_this=pk),
    }
    return render(request, 'forum/forum_instance.html', data)


class CreateYourPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePost
    template_name = 'forum/your_self_topic.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateYourPost, self).get_context_data(**kwargs)
        ctx['title'] = 'Создать пост'
        return ctx
