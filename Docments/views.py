from django.shortcuts import render
from Docments.models import Category,Documents


# Create your views here.


def index(request):
    documents_list = Documents.objects.order_by('full_name')
    content_dict = {'documents': documents_list}

    return render(request, 'documents/index.html', content_dict)


def doc(request,doc_no):
    return render(request, 'documents/doc_detail.html')


def category(request):
    return render(request, 'documents/category.html')


def about(request):
    return render(request, 'documents/about.html')