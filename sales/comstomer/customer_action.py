from common.models import Customer


def query_customer_all(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串
    ret_list = list(qs)

    return ret_list


def save_customer(request):
    info = request.params['data']
    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = Customer.objects.create(name=info['name'],
                                     phone_number=info['phone_number'],
                                     adder=info['adder'])
    return record.id


def modify_customer_by_id(request):
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作
    customerid = request.params['id']
    newdata = request.params['newdata']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{customerid}`的客户不存在'
        }
    if 'name' in newdata:
        customer.name = newdata['name']
    if 'phone_number' in newdata:
        customer.phone_number = newdata['phone_number']
    if 'address' in newdata:
        customer.adder = newdata['adder']
    # 注意，一定要执行save才能将修改信息保存到数据库
    customer.save()


def del_customer_by_id(request):
    customerid = request.params['id']
    try:
        # 根据 id 从数据库中找到相应的客户记录
        customer = Customer.objects.get(id=customerid)
    except Customer.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{customerid}`的客户不存在'
        }
    # delete 方法就将该记录从数据库中删除了
    customer.delete()
