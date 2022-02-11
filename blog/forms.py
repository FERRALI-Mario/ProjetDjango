from django import forms

from blog.models import Comment, Post


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=2000,
        label=False,
        widget=forms.Textarea(attrs={'placeholder': 'Commentaire'}),
        required=True,
    )

    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(attrs={'placeholder': 'Titre'}),
        required=True,
    )
    content = forms.CharField(
        max_length=2000,
        label=False,
        widget=forms.Textarea(attrs={'placeholder': 'Description', 'rows': 5, 'cols': 37}),
        required=True,
    )
    CHOICES = [('1', 'Hiver'), ('2', 'Ete'), ('3', 'Automne'), ('4', 'Printemps')]
    category = forms.ChoiceField(
        label=False,
        choices=CHOICES,
        required=True,
    )

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'category',
        )
