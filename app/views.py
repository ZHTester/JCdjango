from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


class TestOne(View):
    def get(self, request, message):
        # message = request.GET.get('message','这里没有输出内容')
        return HttpResponse(message)

#
# def index(request,name,age):
#     # name = request.GET.get('name', '')  # 形式传参法
#     # age = request.GET.get('age', 0)
#
#     return HttpResponse("hello i am {0} my age is {1}".format(name,age))   # 形式传参法


