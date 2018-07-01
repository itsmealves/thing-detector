# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
import keras
import numpy as np
from PIL import Image
from keras.applications import resnet50
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
from django.core.files.storage import default_storage
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
    def run_detection(self, file):
        image = Image.open(file.file).resize((224, 224))

        resnet_model = resnet50.ResNet50(weights='imagenet')
        matrix = img_to_array(image)
        image_batch = np.expand_dims(matrix, axis=0)
        processed_image = resnet50.preprocess_input(image_batch.copy())
        predictions = resnet_model.predict(processed_image)

        print(decode_predictions(predictions))

        return file


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
        file = self.run_detection(request.FILES['file'])
        key = uuid.uuid4().hex[0:20]
        file_name = str(uuid.uuid4()) + '.' + file.name.split('.')[-1]


        with default_storage.open(file_name, 'w') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        url = default_storage.url(file_name).split('?')[0]

        new_detection = Detection(key=key, url=url)
        new_detection.save()

        return JsonResponse({
            'url' : url,
            'key' : key
        })
