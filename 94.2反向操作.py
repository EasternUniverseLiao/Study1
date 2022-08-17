def use_info(a,b,c) :
    print(a,b,c)

use_info(*(1,2,3))#此时*表示解包
use_info(*[1,2,3])
use_info(*{1,2,3})