from django.urls import path
from .views import index, index2, index3, index4,\
    index5, index6, index7, index8, index9

app_name = 'source'

urlpatterns = [
    path('', index, name='index'),
    path('page-2/', index2, name='index2'),
    path('page-3/', index3, name='index3'),
    path('page-4/', index4, name='index4'),
    path('page-5/', index5, name='index5'),
    path('page-6/', index6, name='index6'),
    path('payment-page/', index7, name='payment'),
    path('page-8/', index8, name='index8'),
    path('page-9/', index9, name='index9')
]


