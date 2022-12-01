from django import forms


class FileUploadForm(forms.Form):
    file_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your file name'}))
    files_data = forms.FileField(widget=forms.FileInput(
        attrs={'accept': '.csv'}))
