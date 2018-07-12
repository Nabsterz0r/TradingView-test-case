from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'^symbols/list', views.SymbolsList, base_name='list')
router.register(r'^symbols/data', views.SymbolsData, base_name='data')

urlpatterns = [
    url(r'^', include(router.urls))
]