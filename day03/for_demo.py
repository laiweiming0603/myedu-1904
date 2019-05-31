# 打印5次hello worlg
def for_demo():
    for i in range(5):
        print('hello world')
        print(i)
def for_demo1():
    # 两个参数时：从第一个参数开始计数，到第二个参数的前一位停止
    for i in range(5,10):
        print('hello world')
        print(i)
def for_demo2():
    # 三个参数时：从第一个参数开始计数，到第二个参数的前一位停止，每次循环递增参数三（步长)
    for i in range(5,10,2):
        print('hello world')
        print(i)
    for i in range(15,10,-2):
        print(i)
# 遍历 list
def for_demo3():
    alist=['ni','hao','xiao',3,5]
    # 方式一
    for i in alist:
        print(i)
    # 方式二
    for i in range(len(alist)):
        print(alist[i])
# 嵌套循环
def for_for():
    # end='xxx':让print以什么内容结尾
    # \n:就是换行符
    # print默认以换行符结尾
    for i in range(5):

        print('你好')
        for j in range(2):
            print('世界',end='啊')
        print('\n')
def break_continue():
    for i in range(5):
        print(i)
        if i ==2 :
            break   #终止所有循环
    for i in range(5):
        if i ==2 :
            continue #终止本次循环，直接进入下一次循环
        print(i)

if __name__ == '__main__':
    for_demo3()
    for_for()
    break_continue()