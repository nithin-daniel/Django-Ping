from rest_framework.views import APIView
from .models import url
from .serializers import urlSerializer
from rest_framework import viewsets
from django.http import HttpResponse
import os 


class urllistapi(viewsets.ModelViewSet):
    serializer_class = urlSerializer
    def create(self,request,*args, **kwargs):
        
        url = request.data.get('url')
        response = os.system("ping -c 1 " + url)

            #and then check the response...
        if response == 0:
            return HttpResponse('Website is on live')
            #  print(url, 'is up!')
        else:
            return HttpResponse('Website is not in live')
            #  print(url, 'is down!')

