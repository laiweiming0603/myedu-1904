import os
# os:获取目录os，权限

if __name__ == '__main__':
    # 获取当前路径
    pwd = os.getcwd()
    print(pwd)
    # 获取上层路径
    shangcengmulu = os.path.abspath('..')
    print(shangcengmulu)
    # 获取上上层路径
    sscengmulu=os.path.abspath('../..')
    print(sscengmulu)


