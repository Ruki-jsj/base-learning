import torch
'''
x=torch.empty(5,3)
print(x)
5*3未初始化的tensor

x=torch.rand(5,3)
print(x)
5*3随机初始化tensor

x=torch.zeros(5,3,dtype=torch.long)
print(x)
创建5*3的long型全0的tensor

x=torch.tensor([5.8,3])
print(x)
直接创建数据tensor

x=torch.tensor([5.5,3])
x=x.new_ones(5,3,dtype=torch.float64)
print(x)
x=torch.rand_like(x,dtype=torch.float)
print(x)
print(x.shape)
print(x.size())
'''
'''
x=torch.rand(5,3)
y=torch.rand(5,3)
print(x+y)
print(torch.add(x,y))
result=torch.empty(5,3)
torch.add(x,y,out=result)
print(result)
#将x加到y
y.add_(x)
#y.add_()将所得的结果存储到原来的y中。torch中所有带'_'的操作都是in_place操作
print(y)
y=x[0,:]
y+=1
print(y)
print(x[0,:])
y=x.view(15)
z=x.view(-1,5)
print(x.size(),y.size(),z.size())
x+=1
print(x)
print(y)
'''
'''
if torch.cuda.is_available():
    device=torch.device("cuda")
    y=torch.ones_like(x,device=device)
    x=x.to(device)
    z=x+y
    print(z)
    print(z.to("cpu",torch.double))
#用方法to（）可以将tensor在cpu和gpu之间相互移动
'''