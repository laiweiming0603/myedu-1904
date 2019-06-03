class people (object):
    def  __init__(self,name,shuxing,jineng):
        self.name=name
        self.shuxing=shuxing
        self.jineng=jineng
    def happy(self):
        print(self.name+'dadoudou')
    def info(self):
        print('一个英雄叫%s，属性是%s，技能为%s'%(self.name,self.shuxing,self.jineng))
class adc(people):
    def __init__(self,name,shuxing,jineng,weizhi):
        self.name = name
        self.shuxing = shuxing
        self.jineng = jineng
        self.weizhi =weizhi
    def info(self):
        print('一个英雄叫%s，属性是%s，技能为%s,位置是%s'%(self.name,self.shuxing,self.jineng,self.weizhi))
    def happy(self):
        print(self.name+'玩手机')

if __name__ == '__main__':
    # xianyu = people('田鱼', '咸鱼', '咸鱼突刺')
    # xianyu.info()
    # xianyu.happy()
    xialu=adc('田鱼', '咸鱼', '咸鱼突刺','adc')
    xialu.info()
    xialu.happy()
