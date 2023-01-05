from io import BytesIO

from django.contrib.auth.models import User, Group
from django.core.files import File
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view

from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def img_upload(request):
    permissions_class = (IsAuthenticated, )
    if request.method == 'POST':
        serializer = ImageSerializer(data={'img1': request.data['img'], 'img2': request.data['img'],
                                           'img3': request.data['img'], 'img4': request.data['img'] })
        if serializer.is_valid():
            serializer.save()
            return Response('Saved Successful')
        else:
            return Response(serializer.errors)
    if request.method == 'GET':
        return Response('Upload Image')
