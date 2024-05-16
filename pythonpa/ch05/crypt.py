from itertools import cycle  #导入模块
def crypt(text, key):
    result = []       #创建一个空列表
    keys = cycle(key) #使用itertools.cycle(key)构造一个循环字符串迭代器keys
    for ch in text:    #循环处理text的每个字符，使用keys中对应字符按位逻辑异或运算
        result.append(chr(ord(ch)^ord(next(keys))))  #将处理后的元素追加到列表的尾部
    return ''.join(result)  #将列表中的各个元素组合为字符串
#测试代码
if __name__=='__main__':
    plain = 'The quick brown fox jumps over the lazy dog' #明文字符串
    key = 'Python_1'                               #秘钥字符串
    print('加密前明文：{}'.format(plain))
    encrypted = crypt(plain, key)                 #字符串加密
    print('加密后密文：{}'.format(encrypted))
    decrypted = crypt(encrypted, key)             #字符串解密
    print('解密后明文：{}'.format(decrypted))
