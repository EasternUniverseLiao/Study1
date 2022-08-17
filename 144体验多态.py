class Dog(object):
    """警犬类"""
    def work(self):
        """父类提供统一的方法，哪怕是空方法"""
        print('指哪打哪...')


class ArmyDog(Dog):  # 继承Dog类
    """追击人的警犬"""

    def work(self):
        """子类重写父类的同名方法"""
        print('追击敌人...')


class DrugDog(Dog):
    """追查毒品的警犬"""

    def work(self):
        """工作是追查毒品"""
        print('追差毒品...')


class Person(object):
    """警务人员对象"""

    def work_with_dog(self, dog):  # 传入不同的对象，执行不同的代码，即不同的work函数
        """dog是形参"""
        dog.work()  # 执行的是哪一个work呢？看下面


ad = ArmyDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)  # 传入的对象是那个类创建的就执行那个类的work方法
daqiu.work_with_dog(dd)
