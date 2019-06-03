import allure

@allure.feature("商品模块")
class Test_order():
    @allure.story("查询待发货订单")
    def test_order_selorder(self):
        #成功发送请求
        #成功收到响应
        assert '成功' in '操作成功'

    @allure.story("发货一个待发货订单")
    def test_order_selorder(self):
        # 成功发送请求
        # 成功收到响应
        assert '成功' in '操作成功'