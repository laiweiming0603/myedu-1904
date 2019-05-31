import json

# 新建一个字典
adict={"username":"admin","password":"123456"}
def dict_sel():
    # 字典是无序的，没有索引，只能通过key去查看，并且key不可重复
    print(adict["username"])
def dict_updete():
    # 只能通过key去更改v
    adict["username"]='laiwm'
    print(adict)
def dict_del():
    adict.pop("username")
    print(adict)
# 增加字典里的键值对
def dict_add():
    adict['age']=18
    print(adict)
    # 合并方式一
    c_dict={'list':[1,2,3],'tuple':(5,6,7)}
    adict.update(c_dict)
    print(adict)
    e_dict={'age':30,'asd':555}
    adict.update(e_dict)
    print(adict)
    # 合并方式二
    d_dict={'age':20,'class':1904}
    g_dict=dict(adict,**d_dict)
    print(g_dict)
# 转换字典类型
def dict_zhuanhuan():
    print(type(adict))
    # 将字典类型转换成字符串
    str_dict= json.dumps(adict,ensure_ascii=False)
    print(str_dict)
    print(type(str_dict))
    # 将字符串转换成字典类型
    str_1='{"username":"admin","password":"123456"}'
    dict_str=json.loads(str_1)
    print(dict_str)
    print(type(dict_str))

if __name__ == '__main__':
    # dict_sel()
    dict_updete()
    # dict_del()
    # dict_add()
    dict_zhuanhuan()