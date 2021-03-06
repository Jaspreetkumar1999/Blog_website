from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User  
from django.views.generic import ListView ,DetailView , CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin 
from  .forms import UserDataForm
def home(request):
    context = {
        'posts': Post.objects.all()
        }
    # return HttpResponse('<h1>blog home </h1>')
    return render(request,'blog/home.html',context )


class PostListView(ListView):
    model = Post
    template_name ='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #to order the content according to the date
    paginate_by = 5  

class UserPostListView(ListView):
    model = Post
    template_name ='blog/user_post.html'
    context_object_name = 'posts'
    # ordering = ['-date_posted'] #to order the content according to the date
    paginate_by = 5 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        #if user exist then we will grab it in the user variable if don't exist then just return 404
        return Post.objects.filter(author = user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields =['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields =['title','content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    # all the mixins should be in the left 
    model = Post
    success_url ='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
   



def about(request):
    form = UserDataForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request,'blog/about.html')
 