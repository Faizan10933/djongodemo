from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),  
    path("", views.ind, name="blogHome"),
    path("todo/<int:id>", views.work, name='work'),    

]
