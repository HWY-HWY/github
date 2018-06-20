from django.shortcuts import render
# Create your views here.
from myapp.models import books


def index(request):
    # pk = request.GET.get("pk")
    # print(pk)
    book_data = books.objects.filter(pk=3).values()
    print(book_data)
    return render(request, "index.html", {'data': book_data[0]})


def blog(request):
    pk = request.GET.get("pk")
    book_info = books.objects.filter(pk=pk).values()
    print(book_info)
    return render(request, 'blog.html', {'data': book_info[0]})


