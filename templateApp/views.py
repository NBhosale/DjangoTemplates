from django.shortcuts import render

# Create your views here.

def base(request):
    baseDir = {"base_injest": "I am base index!"}
    return render(request, 'templateProject/base.html', context=baseDir)

def index(request):
    indexDir = {"index_injest": "I am inside index!"}
    return render(request, 'templateProject/index.html', context=indexDir)

def other(request):
    otherDir = {"other_injest": "I am inside other!"}
    return render(request, 'templateProject/other.html', context=otherDir)

def relativeURL(request):
    relativeUrlDir = {"relativeURL_injest": "I am relative URL template index!"}
    return render(request, 'templateProject/relative_url_templates.html', context=relativeUrlDir)
