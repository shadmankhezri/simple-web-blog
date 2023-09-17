from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES = ['1980' , '1981' , '1982']
    FAVORITE_COLORS_CHOICES = [
        ("blue", "Blue"),
        ("green", "Green"),
        ("black", "Black"),
    ]

    name = forms.CharField(max_length=500 , label='your name')
    text = forms.CharField(max_length=500 , label='your message')
    birth_year = forms.DateField(widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple() , choices=FAVORITE_COLORS_CHOICES)


    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same' , code='name_text_same')


    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError('a can not be in name' , code='a_in_name')
    #     return name


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = ('title' , 'text' , 'email')
        fields = '__all__'

        widgets = {
            "title":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"enter your title",
                "style":"max-width:300px;"
            }),
            "text":forms.Textarea(attrs={
                "class":"form-control"
            })
        }

























