# 所谓的包就是一个文件夹，这个文件夹存放的是有联系的模块，
# 创建方式：[File]--[New]--[Packge]
# 新建包后，包的内部自动创建__init__.py文件，用来控制包的导入行为

# 方法一：
# import 包名.模块名（导入模块）
# 包名.功能名.方法名（调用）

import mypackage.my_module1

mypackage.my_module1.info_print1()


# 方法二：（注意必须在__init__.py文件中添加__all__ = [],控制允许导入的模块列表）
# from 包名 import *
# 模块名.目标

from mypackage import *
my_module1.info_print1()
# my_module2.info_print2()#这个在all列表没有
