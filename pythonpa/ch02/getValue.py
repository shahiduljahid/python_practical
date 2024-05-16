def getValue(b,r,n):          #创建函数对象getValue
    v = b*((1+r)**n)        #计算最终收益v
    return v               #使用return返回值
b=1000;r=0.05;n=5
total = getValue(b, r, n)  #调用函数getValue()
print(f"本金：{b}, 年利率：{r:0.2%}，存期：{n} 年, 本金复利息和：{total:8.2f}")
