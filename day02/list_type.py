alist=['ss',111,'bala','你好',321]
# 访问list
def list_sel():
    # 通过索引访问，从0开始
    print(alist[0])
    # 通过倒序访问，从-1开始
    print(alist[-3])
    # 通过切片访问，前索引值：后索引值
    print(alist[2:3])
def list_del():
    # 不填参数，默认删除最后一位索引内容
    alist.pop()
    print(alist)
    # 填写参数，删除指定索引内容，并把删除的元素提取出来，赋值给a
    a=alist.pop(0)
    print(alist)
    print(a)
def list_add():
    # 默认添加在末尾
    alist.append('我是')
    print(alist)
    b_list=['田鱼','小蜜蜂',123]
    alist.append(b_list)
    print(alist)
    # 合并两个数组的元素
    alist.extend(b_list)
    print(alist)
def list_update():
    alist[0] = '小蜜蜂'
    print(alist)
    alist[2] = 200
    print(alist)
    alist[0:2] = '我',6
    print(alist)
    alist[1:3] = 'haha','xixi'
    print(alist)
def list_order_by():
    b_list=[3,6,4,5,1,8,7,3,3]
    # 默认从小到大排序
    b_list.sort()
    print(b_list)
    # 从大到小排序
    b_list.sort(reverse=True)
    print(b_list)
    b_list.append(2)
    # 从小到大排序
    b_list.sort(reverse=False)
    print(b_list)
def list_distinct():
    c_list=[1,3,2,2,5,6,9,4,2,7,8]
    c_list=set(c_list)
    print(c_list)
    c_list = list(set(c_list))
    print(c_list)
    # 获取长度
    print(len(c_list))


if __name__ == '__main__':
    list_sel()
    # list_del()
    list_add()
    # list_update()
    # list_order_by()
    list_distinct()
