from django.contrib import admin
from django.urls import path
from mainApp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.homes),
    path('delete/<int:id>',views.delete),
    path('add/',views.addRecord),
    path('update/<int:id>',views.updateRecord),
]
