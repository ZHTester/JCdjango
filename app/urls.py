from django.urls import path
from .views import TestOne

urlpatterns = [
    # path('<str:name>/<int:age>',index),
    path("two/<str:message>", TestOne.as_view(), name='two')
]