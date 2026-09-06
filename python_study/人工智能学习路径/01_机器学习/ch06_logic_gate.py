import numpy as np
# #实现与门
# def AND(x1,x2):
#     w1,w2,theta=0.5,0.5,0.7
#     res=x1*w1+x2*w2
#     return 1 if res >= theta else 0
# print(AND(0,0))
# print(AND(0,1))
# print(AND(1,0))
# print(AND(1,1))
def AND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.7
    #直接矩阵预算
    res=w@x+b
    return 0 if res<=0 else 1
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
#与非门
def NAND(x1,x2):
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    #直接矩阵预算
    res=w@x+b
    return 0 if res<=0 else 1
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))
def OR(x1,x2):
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=0
    res=w@x+b
    return 0 if res<=0 else 1
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))
#异或门
def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))
