from django.contrib import admin
from django.urls import path
from myapp2 import views

urlpatterns = [
    path('hello/',views.hello,name='hello'),
    path('hungerg1/',views.hungerg1,name='hungerg1'),
    path('owner/',views.owner,name='owner'),
    path('add_newbook/',views.add_newbook, name='add_newbook'),
    path('owner/mainweb/<int:id>',views.mainweb,name='mainweb'),
    path('owner/mainweb/update/<int:id>/',views.update,name='update'),
    path('owner/mainweb/buy/<int:id>/',views.buy,name='buy')
]