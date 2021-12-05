from django import forms
from blog.models import Post
class ContactForm(forms.Form):
    Name = forms.CharField()
    Age = forms.IntegerField()
    email = forms.EmailField()
    Phoneno = forms.IntegerField() 
    Query = forms.CharField(widget=forms.Textarea)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Title','Content','Type')
