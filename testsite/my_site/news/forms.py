from django import forms
from news.models import Category, News


# class NewsForm(forms.Form):
#    title = forms.CharField(max_length=130, required=False,
#                            label='Название новости',
#                            widget=forms.TextInput(attrs={'class': 'form-control'})
#                            )
#    content = forms.CharField(label='Текст',
#                              widget=forms.Textarea(attrs={'class': 'form-control',
#                                                           'rows': 4})
#                              )
#    photo = forms.ImageField(required=False, label='Загрузить фото')
#    category = forms.ModelChoiceField(empty_label='Выберите категории',
#                                      queryset=Category.objects.all(),
#                                      label='Категория',
#                                      widget=forms.Select(attrs={'class': 'form-control'})
#                                      )
#    is_published= forms.BooleanField(label='Опубликовать', required=False)
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'photo', 'category', 'is_published']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),

                   'category': forms.Select(attrs={'class': 'form-control'}),

                   }
