# Create your views here.
from django.http import HttpResponse, JsonResponse

# from django_simple.common.models import Customer
# from .. import common
from common.models import Customer


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


def query_customer(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    ret_list = list(qs)

    return JsonResponse({'ret': 0, 'retlist': ret_list})


def add_customer(request):
    pass


def modify_customer(request):
    pass


def del_customer(request):
    pass
