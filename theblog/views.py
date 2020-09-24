from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from . models import Post, Category
from . forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect



# def Home(request):
# 	return render(request, 'theblog/home.html',{})

def LikeView(request, pk):
	post = get_object_or_404(Post,id=request.POST.get('post_id'))
	
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))

class HomeView(ListView):
	model = Post
	template_name = "theblog/home.html"
	# ordering = ['-id']
	ordering = ['-post_date','-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


class ArticleDetailView(DetailView):
	model = Post
	template_name = "theblog/article_details.html"


	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		
		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context['total_likes'] = total_likes
		context['liked'] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'theblog/add_post.html'
	# fields = "__all__"
	# fields = ("title", 'body')

	# def get_context_data(self, *args, **kwargs):
	# 	cat_menu = Category.objects.all()
	# 	context = super(AddPostView, self).get_context_data(*args, **kwargs)
	# 	context["cat_menu"] = cat_menu
	# 	return context

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'theblog/update_post.html'
	# fields = ['title','title_tag', 'body']


	# def get_context_data(self, *args, **kwargs):
	# 	cat_menu = Category.objects.all()
	# 	context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
	# 	context["cat_menu"] = cat_menu
	# 	return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'theblog/delete_post.html'
	success_url = reverse_lazy('home')


	# def get_context_data(self, *args, **kwargs):
	# 	cat_menu = Category.objects.all()
	# 	context = super(DeletePostView, self).get_context_data(*args, **kwargs)
	# 	context["cat_menu"] = cat_menu
	# 	return context

class AddCategoryView(CreateView):
	model = Category
	# form_class = CategoryForm
	template_name = 'theblog/add_category.html'
	fields = "__all__"
	# fields = ("title", 'body')

	# def get_context_data(self, *args, **kwargs):
	# 	cat_menu = Category.objects.all()
	# 	context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
	# 	context["cat_menu"] = cat_menu
	# 	return context

def CategoryView(request,category):
	posts = Post.objects.filter(category=category.replace('-',' '))
	cats = Category.objects.all()

	context = {
	 'posts':posts,
	 'cat_menu':cats,
	 'category':category.replace('-',' '),
	}
	return render(request, 'theblog/categoryview.html',context)

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	context = {
	 'cat_menu':cat_menu_list,
	}
	return render(request, 'theblog/category_list.html',context)