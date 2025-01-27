from django.contrib import admin
from django.urls import path
from Home import views


admin.site.site_header = 'ShAnGgAi'
admin.site.site_title = 'ShAnGgAi'

admin.site.index_title = 'ShAnGgAi Admin Panel'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('About', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('BookATable', views.BookATable, name='BookATable'),
]
