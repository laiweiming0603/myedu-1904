def open_write():
    # open('文件地址文件名'，'打开方式')
    # w+覆盖之前内容
    text_io = open('lala.txt', 'w+')
    for i in range(5):
        text_io.write('田鱼，小蜜蜂\n' )
def open_write1():
    # a+追加之前内容
    text_io = open('lala.txt', 'a+')
    for i in range(5):
        text_io.write('田鱼，lowbee\n' )
def open_read():
    text_io= open('lala.txt', 'r')
    # 读取所有行，返回一个list
    # print(text_io.readlines())
    # 读取第一行
    print(text_io.readline())
if __name__ == '__main__':
    # open_write1()
    open_read()
