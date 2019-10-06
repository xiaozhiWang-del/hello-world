a=eval(input("输入第1个数字"))
b=eval(input("输入第2个数字"))
c=eval(input("输入第3个数字"))
print("输入顺序为：",a,b,c)
if a<b:
    a,b=b,a
if a<c:
    print("排序后为：",c,a,b)
else:
    if b<c:
        print("排序后为：",a,c,b)
    else:
        print("排序后为：",a,b,c)

  