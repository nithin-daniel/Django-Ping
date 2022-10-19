from rest_framework.views import APIView
from .models import url
from .serializers import urlSerializer
from rest_framework import viewsets
import os 
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
import urllib.request
from urllib.request import urlopen
from urllib.error import *


class urllistapi(viewsets.ModelViewSet):
    serializer_class = urlSerializer
    def create(self,request,*args, **kwargs):
        
        url = request.data['url']
        print(url)
        # response = os.system("ping -c 1 " + url)
        # print(response)


        # try block to read URL
        try:
            html = urlopen(url)
            
        # except block to catch
        # exception
        # and identify error

            
        except URLError as e:
            print("Opps ! Page not found!", e)
            return HttpResponse("Opps ! Page not found!")
        
        else:
            print('Yeah !  found ')
            return HttpResponse('Yeah !  found ')






