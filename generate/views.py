from django.shortcuts import render, HttpResponse
from forms import StarterPackForm
import urllib
import os
from django.conf import settings
from PIL import Image, ImageDraw,ImageFont

from django.core.files import File
from random import randint
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = StarterPackForm(request.POST)
        if form.is_valid():
            links = [urllib.urlretrieve(form.cleaned_data['link'+str(x)]) for x in range(1,5)]
            images = [Image.open(x[0]) for x in links]
            images = [x.resize((320,320)) for x in images]
            boxes = [(0,0),(320,0),(0,320),(320,320)]
            print images
            im = Image.new('RGB',(640,640))
            for image,box in zip(images,boxes):
                im.paste(image,box)
            #return HttpResponse("YAY")
            title = form.cleaned_data['title']
            font = ImageFont.truetype("static/arial.ttf", 40)

            draw = ImageDraw.Draw(im)
            w,h = draw.textsize(title)


            draw.text((320-(w),0),title,fill=(0,0,0),font=font)
            del draw
            response = HttpResponse(content_type="image/png")
            # now, we tell the image to save as a PNG to the
            # provided file-like object
            im.save(response, 'PNG')

            return response # and we're done!

    else:
        form = StarterPackForm()
        context = {}
        context['form'] = form
        return render(request, 'index.html',context)

def save(image,unique_id,number):
    path=os.path.join('uploaded')
    new_path = os.path.join(settings.MEDIA_ROOT,path)
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    new_path = os.path.join(new_path,unique_id)
    os.mkdir(new_path)
    filename = 'image'+str(number)
    filepath = os.path.join(str(new_path), str(filename))

