from django import forms
from . models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','snippet','category','body','header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
			'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
			'author': forms.TextInput(attrs={'class':'form-control', 'value':'','id':'author','type':'hidden'}),
			'snippet': forms.TextInput(attrs={'class':'form-control'}),
			'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Details'}),
		} 


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag', 'category','snippet','body','header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Title'}),
			'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Blog Tag'}),
			'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
			'snippet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Snippet'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Blog Details'}),
		} 

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}),
			} 