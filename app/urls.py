from django.urls import path
# from .views import TestOne
from .views import IndexView

urlpatterns = [
    # path('<str:name>/<int:age>',index),
    # path("two/<str:message>", TestOne.as_view(), name='two'),
    path('<str:name>', IndexView.as_view(), name='indexs')
]