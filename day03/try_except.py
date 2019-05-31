if __name__ == '__main__':
    # try和except之间写可能会出错的代码
    # 如果出错则执行except下得代码,不影响其他代码执行
    try :
        print('报错之前')
        a=5/0
    except:
        print('报错')
    print('lalala')