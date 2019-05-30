# 题: 新建一个list变量,里面有五个元素,访问索引2,切片访问索引1到4,删除索引3,添加两个元素,第0位元素改成字符5,获取索引长度
alist=[1,6,3,2,4,5]
adict={"田鱼":"小蜜蜂","九阳":"神功","bala":"nengliang"}
def list_order():
    alist.sort()
    print(alist)
def list_sel():
    print(alist[2])
    print(alist[1:4])
def list_del():
    alist.pop(3)
    print(alist)
def list_add():
    alist.append(7)
    alist.append(8)
    print(alist)
    b_list=[9,10]
    alist.extend(b_list)
    print(alist)
    print(len(alist))
def list_update():
    alist[0]='5'
    print(alist)
def dict_sel():
    print(adict["田鱼"])
def dict_del():
    bdict = adict.pop("bala")
    print(adict)
    print(bdict)
def dict_update():
    adict["田鱼"]="小小蜜蜂"
    print(adict)
if __name__ == '__main__':
    list_order()
    list_sel()
    list_del()
    list_add()
    list_update()
    dict_sel()
    dict_del()
    dict_update()