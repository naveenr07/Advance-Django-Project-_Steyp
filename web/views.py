from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context=context)


def send_files(request):
    if request.method == 'POST':
        name = request.POST.get()
