def if_demo():
    # 一个等号是赋值，两个等号是相等
    a= 3-2==1
    if a :
        print('a是正确的')
    else:
        print('a是错误的')
def elif_demo():
    a=10-5
    if a==1:
        print('a等于1')
    elif a==2:
        print('a等于2')
    elif a==3:
        print('a等于3')
    elif a==5:
        print('a等于5')
    else:
        print('a不等于1,2,3,4啊')

if __name__ == '__main__':
    # if_demo()
    elif_demo()
