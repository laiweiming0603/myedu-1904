# 1-50之间奇数和
# 取余，自增
# 打印九九乘法表
# 打印两个数之间的偶数和

# 有一个篮子,里面有若干鸡蛋,
# 每次拿 4 个 最后剩一个,
# 每次拿五个剩四个,
# 每次拿6个 最后剩3个,
# 每次拿七个最后剩5个,
# 每次拿八个最后剩一个,
# 每次拿九个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
def jidan():
    for i in range(1,1001):
        if i % 4==1:
            if i % 5==4:
                if i%6==3:
                    if i %7==5:
                        if i%8==1:
                            if i%9==0:
                                print(i)

def for_jishu():
    a=0
    for i in range (1,51):
        if i % 2==1:
            a+=i
    print(a)
def jiujiu():
    for i in range(1,10):
        a=i+1

        for j in range(1,a):
            print('%s*%s=%s'%(j,i,j*i),end='  ')

        print('')

def oushu():
    a = 0
    for i in range(1, 11):
        if i%2==0:
            a+=i
    print(a)

if __name__ == '__main__':
    # for_jishu()
    # jiujiu()
    # oushu()
    jidan()
