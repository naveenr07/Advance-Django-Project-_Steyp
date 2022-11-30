import json
from django.shortcuts import render, HttpResponse

from .forms import FileUploadForm
from .models import FileUploads


def index(request):

    if request.method == 'POST':
        client_form = FileUploadForm(request.POST, request.FILES)

        if client_form.is_valid():
            name = client_form.cleaned_data['file_name']
            files = client_form.cleaned_data['files_data']
            FileUploads(file_name=name, my_files=files).save()
            response_data = {
                "title": "Successfully submitted",
                "message": "Successfully submitted",
                "status": "success",
            }
            return HttpResponse(json.dumps(response_data), content_type='application/json')
        else:
            return HttpResponse("error")
    else:
        context = {
            'form': FileUploadForm()
        }
        return render(request, "index.html", context=context)


def show_file(request):
    all_data = FileUploads.objects.all()

    context = {
        'data': all_data
    }

    return render(request, 'view.html', context)
