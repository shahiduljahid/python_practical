#求解m和n的最大公约数。GCD(m, n) = GCD(n, m Mod n)
def gcd(m,n):
    if (m < n):
        m, n = n, m
    while (n != 0):
        m, n = n, m%n
    return m
if __name__ == '__main__':
    print(24,36,"的最大公约数为：",gcd(24,36))


'''
        remainder = m % n    # 计算余数
        m = n
        n = remainder
'''
