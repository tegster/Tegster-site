import torch
import numpy as np
#
# Pytorch Tensors https://pytorch.org/docs/stable/tensors.html
# Notes by Tegster
# 
# 1D tensors

tensor1D = torch.tensor([1,2,3,4,5,6])
print(tensor1D) # tensor([1, 2, 3, 4, 5, 6])
print(tensor1D.dtype) #print tensor datatype, # torch.int64
print(tensor1D[1]) #print tensor by index, # tensor(2)
print(tensor1D[3]) #print tensor by index, # tensor(4)
print(tensor1D[1:4]) # tensor([2, 3, 4])
print(tensor1D[1:]) # tensor([2, 3, 4, 5, 6])

tensor1D = torch.tensor([1,2,3,4,5,6])
floatTensor = torch.FloatTensor([1,2,3,4,5,6])

print(floatTensor) # tensor([1., 2., 3., 4., 5., 6.])
print(floatTensor.dtype) # torch.float32
print(floatTensor.size()) # torch.Size([6])

# View of an existing tensor, 
# View avoids explicit data copy, 
# allows us to do fast and memory efficient reshaping, slicing
print(tensor1D.view(6,1))
# tensor([[1],
#         [2],
#         [3],
#         [4],
#         [5],
#         [6]])
#
# The negative one implies a value will be inferred based on length 
# of tensor, All the below produce the same value
print(tensor1D.view(3,2))
print(tensor1D.view(3,-1))
print(tensor1D.view(-1,2))
# tensor([[1, 2],
#         [3, 4],
#         [5, 6]])

# Converting a Numpy Array 
nparray = np.array([1,2,3,4,5,6])
numpytensor = torch.from_numpy(nparray)
print(nparray) # [1 2 3 4 5 6]
print(numpytensor) # tensor([1, 2, 3, 4, 5, 6], dtype=torch.int32)

tensor_numpy_cnv = numpytensor.numpy()
print(tensor_numpy_cnv) # [1 2 3 4 5 6]
