#不定长关键字写法：收集所有关键字参数返回一个字典


#包裹关键字传递
def use_info(**kwargs):
    print(kwargs)


use_info()#返回空字典
use_info(name='Tom')#key不用引号
use_info(name='Tom',age=18,id=110)#这就是个组包的过程