import os
from random import random
from django.conf import settings
from django.shortcuts import render

from datetime import datetime
from PIL import Image
from MY_DEMO.settings import BASE_DIR

from Search.forms import SearchForm
# Create your views here.

STATIC_ROOT = os.path.join(BASE_DIR, "_data/")


def index(request):
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST, request.FILES)
        if search_form.is_valid():

            # Nhận vào ảnh từ form
            img = search_form.cleaned_data['search']
            img = Image.open(img)
            uploaded_img_path = f"{settings.MEDIA_ROOT}/image.png"
            img.save(uploaded_img_path)

            # Trích xuất đặc trưng

            # Trả về kết quả
            folder = f"{STATIC_ROOT}"
            images = []
            for filename in os.listdir(folder):
                img = os.path.join(folder, filename)
                if img is not None:
                    score = random()  # Khoảng cách euclidean
                    images.append({"src": img, "score": score})
            images.sort(key=lambda x: x["score"], reverse=True)
            images = images[:30]

            return render(request, 'index.html', {'search_form': search_form, 'images': images})
    return render(request, 'index.html', {'search_form': search_form})
