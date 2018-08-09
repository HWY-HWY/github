from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.


def ajax(request):
    return render(request, 'Ajax.html')


def ajax_form(request):
    data = {}
    data['status'] = 'SUCCESS'
    data['log_info'] = request.POST['username']
    return JsonResponse(data)