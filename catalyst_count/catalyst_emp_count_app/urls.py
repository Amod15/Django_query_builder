from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('query_data/',views.query_data,name='query_data'),
    path('upload_file_template/',views.upload_file_template,name='upload_file_template'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]
