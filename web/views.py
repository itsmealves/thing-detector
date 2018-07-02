# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from models import Detection

# Create your views here.
def index(request):
    return render(request, 'index.html')

def not_found(request):
    return redirect('/')

class FileView(View):
    def get(self, request):
        key = ''
        url = ''

        try:
            detection = Detection.objects.get(key=request.GET.get('key', ''))

            key = detection.key
            url = detection.url
        except Detection.DoesNotExist:
            pass

        return JsonResponse({
            'url' : url,
            'key' : key
        })


    def post(self, request):
        file = request.FILES['file']

        print(type(file))

        key = uuid.uuid4().hex[0:20]
        extension = file.name.split('.')[-1]
        file_name = str(uuid.uuid4()) + '.' + extension

        files = {'file': file}
        payload = {'filename': file_name}
        response = requests.post('http://localhost:4000', data=payload, files=files).json()
        url = response['url']

        detection = Detection(key=key, url=url)
        detection.save()

        return JsonResponse({
            'url' : url,
            'key' : key
        })
