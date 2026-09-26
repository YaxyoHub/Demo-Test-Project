from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        uzunligi = len(title)
        if uzunligi < 5:
            raise ValidationError('Title 5 ta hafrdan kam bulmasligi kerak!')

        return title
    
        

class Edit_Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image']

