class Color:                       #定义类
    """表示RGB模型的类"""
    def __init__(self, r=0, g=0, b=0):   #构造函数
        """构造函数"""
        self._r = r                  #Red（红色）分量
        self._g = g                 #Green（绿色）分量
        self._b = b                 #Blue（蓝色）分量
    @property
    def r(self):
        return self._r                #返回红色分量
    @property
    def g(self):
        return self._g                #返回绿色分量
    @property
    def b(self):
        return self._b                 #返回蓝色分量
    def luminance(self):
        """计算并返回颜色的亮度"""
        return .299*self._r + .587*self._g + .114*self._b
    def toGray(self):
        """转换为灰度颜色"""
        y = int(round(self.luminance()))    #四舍五入取整
        return Color(y, y, y)
    def isCompatible(self, c):
        """比较前景色和背景色是否匹配"""
        return abs(self.luminance() - c.luminance()) >= 128.0
    def __str__(self):
        """重载方法，输出：(r, g, b)""" 
        return '({},{},{})'.format(self._r,self._g,self._b)
#常用颜色
WHITE      = Color(255, 255, 255)
BLACK      = Color(  0,   0,   0)
RED        = Color(255,   0,   0)
GREEN      = Color(  0, 255,   0)
BLUE       = Color(  0,   0, 255)
CYAN       = Color(  0, 255, 255)
MAGENTA    = Color(255,   0, 255)
YELLOW     = Color(255, 255,   0)
if __name__ == '__main__':     #如果独立运行时，则运行测试代码
    c = Color(255, 200, 0)                          #ORANGE（橙色）
    print('颜色字符串：{}'.format(c))                #输出颜色字符串
    print('颜色分量：r={},g={},b={}'.format(c.r, c.g, c.b)) #输出各颜色分量
    print('颜色亮度：{}'.format(c.luminance()))         #输出颜色亮度
    print('转换为幅度颜色：{}'.format(c.toGray()))      #输出转换后的灰度颜色
print('{}和{}是否匹配：{}'.format(c,RED,c.isCompatible(RED))) #比较与红色是否匹配
