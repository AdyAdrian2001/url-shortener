from django.shortcuts import render_to_response, get_object_or_404, render
from .models import ShortUrl
from django.http import HttpResponseRedirect
from django.views import View
from .forms import SubmitUrlForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "form": the_form,
        }
        return render(request, 'urlshortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "form": form,
        }
        template = "urlshortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortUrl.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "urlshortener/success.html"
            else:
                template = "urlshortener/already-exist.html"

        return render(request,template, context)

class ShortUrlView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortUrl, shortcode=shortcode) # get object, if not found return 404 error
        return HttpResponseRedirect(obj.url)
