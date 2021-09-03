#Youtube tutorial: https://www.youtube.com/watch?v=BzcBsTou0C0
# "Introduction - Deep Learning and Neural Networks with Python and Pytorch p.1"
#Posted by user "sentdex"

import torch

#Recall: a tensor is a multi-dimensional array
#This calculation happens on the CPU
x = torch.Tensor([5,3])
y= torch.Tensor([2,1])

print(x*y)

#torch.zeros and torch.shape are similar to what's in numpy!
x=torch.zeros([2,5])
print(x)
print(x.shape)

y=torch.rand([2,5])
print(y)

#Reshaping the tensor. In numpy and tensorflow, you'd say .reshape.
#In torch, the method for reshaping is called "view"

#flatten the [2,5] to a [1,10] because there are 10 total elements
y.view([1,10]) #does not modify y
print(y)
y=y.view([1,10]) #modified y



