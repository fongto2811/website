from django.shortcuts import render, get_object_or_404
from .models import Pages
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json

def index(request):
    #page = Pages.objects.filter(is_home=True)
    page = get_object_or_404(Pages, slug="trang-ch")
    return render(request, 'index.html', {"page": page})
    

def page(request):
    pages = Pages.objects.all()
    content = {
        'pages': pages,
    }
    return render(request, 'admin/page.html', content)

def addpage(request):
    return render(request, 'admin/grapesjs.html')

def editPage(request, slug):
    #page = get_object_or_404(Pages, slug=slug)
    page = Pages.objects.get(slug=slug)
    #page = Pages.objects.filter(slug=slug)
    content = {
        "page": page,
    }
    return render(request, 'admin/grapesjs.html', content)

def editPageContent(request, slug):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        #page = get_object_or_404(Pages, slug=slug)
        page = Pages.objects.get(slug=slug)
        page.html = html
        page.css = css
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]})

def savePage(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        page = Pages.objects.create(name="untitled", html=html, css=css)
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]}) 

def previewPage(request, slug):
    page = Pages.objects.get(slug=slug)
    return render(request, 'index.html', {"page": page})