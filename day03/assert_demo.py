# 断言
# 断言成功没提示
def assert_int():
    try:
        assert 3<2
    except:
        print('断言失败了')
def assert_str():
    a='你好'
    b={'你好','我是'}
    try :
        assert a in b
        assert a not in b
    except:
        print('断言失败')
if __name__ == '__main__':
    # assert_int()
    assert_str()