# Create your views here.
from django.http import HttpResponse, JsonResponse

# from django_simple.common.models import Customer
# from .. import common
from common.models import Customer
from sales.comstomer.customer_action import query_customer_all, save_customer, modify_customer_by_id, del_customer_by_id


def hello_django(request):
    return HttpResponse("hello django")


def hello_python(request):
    return HttpResponse("hello python")


def list_customers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值

    qs = Customer.objects.values()
    name = request.GET.get("name", None)
    if name is not None:
        qs.filter("name", name)
    # 定义返回字符串
    retStr = ''
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)


"""
 只做简单的调用入口，实现放在 action里,也可以做一下简单的参数校验
 
 测试路径
 GET /sales/api?action=query_customer
"""


def query_customer(request):
    return JsonResponse({'ret': 0, 'retlist': query_customer_all(request)})


def add_customer(request):
    return JsonResponse({'ret': 0, 'id': save_customer(request)})


def modify_customer(request):
    modify_customer_by_id(request)
    return JsonResponse({'ret': 0})


def del_customer(request):
    del_customer_by_id(request)
    return JsonResponse({'ret': 0})
