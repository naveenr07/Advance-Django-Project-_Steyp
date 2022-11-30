from django import forms


class FileUploadForm(forms.Form):
    file_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    files = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control'}))
