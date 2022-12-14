from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, View, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm, ContactForm
from django.contrib import messages


# Create your views here.
class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_date')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(View):

    def get(self, request):
        context = {'form': PostForm()}
        return render(request, 'add_post.html', context)

    def post(self, request):

        if request.method == 'POST':
            form = PostForm(request.POST, initial={
                'author': request.user.username
                })
            if form.is_valid():
                form.instance.email = request.user.email
                form.instance.name = request.user.username
                form.instance.author = self.request.user
                form.save()
                messages.success(request, 'Your post is awaiting approval.')
                return redirect('home')
            else:
                messages.error(
                    request, 'Error: Something went wrong, please try again.')
                context = {'form': form}
                return render(request, 'add_post.html', context)
        else:
            form = PostForm()

        context = {'form': form}
        return render(request, 'index.html', context)


class UpdatePost(UpdateView):

    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content', 'excerpt', 'featured_image']


class DeletePost(DeleteView):

    model = Post
    template_name = 'delete_post.html'
    success_url = '/'


class BlogPosts(ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_date')
    template_name = 'blog_posts.html'
    paginate_by = 6


class Contact(FormView):

    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/'

    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('home')
        else:
            messages.error(request, 'This is not a valid form')
            return redirect('home')
