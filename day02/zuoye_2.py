a_dict={"田鱼":"小蜜蜂","巴啦啦":"能量"}
def dict_sel():
    print(a_dict["田鱼"])
def dict_del():
    a_dict.pop('巴啦啦')
    print(a_dict)
def dict_add():
    a_dict["圣枪游侠"]="卢锡安"
    print(a_dict)
def dict_update():
    a_dict["巴啦啦"]="小魔仙"
    print(a_dict)
def dict_hebing():
    b_dict={"齐天大圣":"孙悟空"}
    a_dict.update(b_dict)
    print(a_dict)
    c_dict=dict(a_dict,**b_dict)
    print(c_dict)
if __name__ == '__main__':
    dict_sel()
    dict_del()
    dict_add()
    dict_update()
    dict_hebing()