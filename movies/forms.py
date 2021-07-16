from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('viewer_rating', 'title', 'comment')
        CHOICES = [
                ('1','1'),
                ('2','2'),
                ('3','3'),
                ('4','4'),
                ('5','5'),
    ]
        widgets = {
            'viewer_rating': forms.RadioSelect(choices=CHOICES),
            'title': forms.TextInput(attrs={
                'placeholder':'Title',
                'class':'form-control'
            }),
            'comment': forms.Textarea(attrs={
                'placeholder':'Enter a comment',
                'class':'form-control',
                'style':'height:8em;'
            })
        }