from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
import datetime



# class TestOne(View):
#     def get(self, request, message):
#         # message = request.GET.get('message','这里没有输出内容')
#         return HttpResponse(message)

#
# def index(request,name,age):
#     # name = request.GET.get('name', '')  # 形式传参法
#     # age = request.GET.get('age', 0)
#
#     return HttpResponse("hello i am {0} my age is {1}".format(name,age))   # 形式传参法

class IndexView(View):
    TEMPLATES = 'index.html'
    
    # def get(self, request,name):
        
    #     return render(request, self.TEMPLATES, {'name':name})
    
    def get(self, request, name):
        data = {}
        data['name'] = name
        data['nums'] = range(0,10)
        data['count'] = 20
        data['times'] = datetime.datetime.now
        data['str_name'] = 'hello-beijing'
        data['capfirst'] = 'capfirst_ding'
        data['default'] = 'False'
        data['default_is_none'] = 'None'
        data['dict_sort'] =[{"name":"xiaoming","age":22},{"name":"xiaoding","age":33}]
        data["html_str"] = "<div style='background-color':red;width:50px;height:50px></div>"
        data['a_str'] = '请看www.baidu.com'
        data['feature'] =  data['times'] 
             
        
        return render(request, self.TEMPLATES, data)


