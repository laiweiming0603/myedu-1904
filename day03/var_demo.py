# 声明一个全局变量
a='你好'
def var_demo():
    print(a)
def var_demo1():
    global a
    a='世界'
    print(a)
if __name__ == '__main__':
    var_demo()
    var_demo1()