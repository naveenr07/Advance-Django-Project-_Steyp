from django.shortcuts import render, HttpResponse

from .forms import FileUploadForm


def index(request):
    context = {
        'form': FileUploadForm()
    }
    return render(request, "index.html", context=context)
