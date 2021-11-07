from django import forms
from boardsApp.models import BoardModel


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class DocumentForm(forms.Form):
    file = forms.FileField(label='Select a file')


class ImageForm(forms.Form):
    image = forms.FileField(label='Select a image')


class BoardForm(forms.Form):
    name = forms.CharField(label='Title ', max_length=100)
    # background = forms.ImageField()


class BoardModelForm(forms.ModelForm):
    class Meta:
        model = BoardModel
        fields = ['name', 'background']

#

# class AddListForm(forms.Form):
#     name = forms.CharField(label='Title ', max_length=100, )
