from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL


def home(request):
    short_url = None

    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        obj = ShortURL.objects.create(original_url=original_url)
        short_url = request.build_absolute_uri('/') + obj.short_code

    return render(request, 'home.html', {'short_url': short_url})


def redirect_url(request, short_code):
    obj = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(obj.original_url)
