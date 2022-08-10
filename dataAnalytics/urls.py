from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name = 'home'),
    # path('ColumnsSelection',views.ColumnsSelection, name='ColumnsSelection'),
    # path('upload',views.upload,name='upload'),
]