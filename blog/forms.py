
from django.forms import ModelForm, SelectDateWidget
from blog.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','mini_text','text','image','created_date']
        widgets = {
            'created_date':SelectDateWidget
        }

create_post_form = PostForm()