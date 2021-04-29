from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from .forms import PostForm

import sweetify


def all_community_posts(request):
    posts = Post.objects.all()

    # posts = {
    #     'title': 'New Post',
    #     'content': 'This is the first test post',
    #     'author': 'Dave',
    #     'date_of_post': 'Today',
    # }
    template = 'community/community.html'

    context = {
        'posts': posts
    }
    
    return render(request, template, context)


def add_post(request):
    '''Post to the community page'''

    if not request.user.is_authenticated:
        sweetify.sweetalert(request, 'Please sign in to post on the form', persistent='Ok')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            sweetify.sweetalert(request, 'Post Success', timer=1000)
            return redirect(reverse('community'))
        else:
            sweetify.sweetalert(request, 'Failed to post.', text='Please ensure the form is valid.', persistent='Ok')
    else:
        form = PostForm()

    template = 'community/add_post.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
