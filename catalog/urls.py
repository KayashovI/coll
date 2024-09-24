from . import views
from django.urls import path
urlpatterns =[
    path('', views.index),
    path('/<int:product_id>',views.product)
]