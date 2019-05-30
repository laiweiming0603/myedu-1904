def add(a,b):
    print(str(a)+str(b))
    return str(a)+str(b)
def aint():
    aint=1
    print(type(aint))
def dda(num1,num2):
    return num1+num2



if __name__ == '__main__':
    # print('hello world')
    c=add('wo','6')
    # print(c)
    # aint()
    d=dda(6,4)
    print(d)
    a='巴啦啦能量乌卡拉'
    print(a[2:])
    print(a[2:4])
    print(a[4:6])
    print(a[3:])
    print(a[-8:])
    print(a[-3:-1])
    print(a[5:7])
    print(a[-5:-3])
    print(a[0]+a[2])
    # 反转
    print(a[:4:-1])