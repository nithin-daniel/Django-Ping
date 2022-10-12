from django.urls import path
from .views import urllistapi
from .views import urllistapi
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('url', viewset=urllistapi)
# urlpatterns = router.urls

urlpatterns = [
    path('api/',urllistapi.as_view({'post': 'create'})),
]














# urlpatterns = [
#     # path('',views.index,name='index'),
#     path('', urllistapi.as_view()),

    
# ]

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'main', urllistapi)
# urlpatterns = router.urls