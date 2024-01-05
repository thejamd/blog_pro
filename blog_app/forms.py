from django import forms
from .models import Post,Category
# choices = [('coding','coding'),('sports','sports'),('Travelling','Travelling')]
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','auther','category','body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title of your blog'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter title_tag of your blog'}),
            'auther': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username','id':'elder'}),
            # 'auther': forms.Select(attrs={'class':'form-control','placeholder':'Enter name of author'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter blog'}),
        }