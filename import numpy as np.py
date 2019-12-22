import numpy as np


def getOutShape(Chin, Chout, Hin, Win, kernel_size, padding, stride):
	Hout = int((Hin + 2*padding[0] - dilation[0] * (kernel_size[0]-1) - 1)/stride[0] + 1)
	Wout = int((Win + 2*padding[1] - dilation[1] * (kernel_size[1]-1) - 1)/stride[1] + 1)
	return Chout, Hout, Wout

def flatten(x):
	return np.product(x)

def upsample(Chin, Hin, Win, scale_factor):
	return Chin, Hin*scale_factor, Win*scale_factor


img_size = (32,32)
dilation = (1, 1)
scale_factor = 2

# conv
x = getOutShape(Chin=1, Chout=7, Hin=img_size[0], Win=img_size[1], kernel_size=(3,3), padding=(1,1), stride=(1,1))
print(x)
# pool
x = getOutShape(Chin=7, Chout=7, Hin=x[1], Win=x[2], kernel_size=(2,2), padding=(0,0), stride=(2,2))
print(x)
# conv
x = getOutShape(Chin=7, Chout=28, Hin=x[1], Win=x[2], kernel_size=(3,3), padding=(1,1), stride=(1,1))
print(x)
# pool
x = getOutShape(Chin=28, Chout=28, Hin=x[1], Win=x[2], kernel_size=(2,2), padding=(0,0), stride=(2,2))
print(x)
x = flatten(x)
print(x)


print('______________________')


img_size = (8,8)

# upsample
x = upsample(Chin=1, Hin=img_size[0], Win=img_size[1], scale_factor=scale_factor)
print(x)
# conv
x = getOutShape(Chin=1, Chout=20, Hin=x[1], Win=x[2], kernel_size=(3,3), padding=(1,1), stride=(1,1))
print(x)
# upsample
x = upsample(Chin=x[0], Hin=x[1], Win=x[2], scale_factor=scale_factor)
print(x)
# conv
x = getOutShape(Chin=x[0], Chout=1, Hin=x[1], Win=x[2], kernel_size=(3,3), padding=(1,1), stride=(1,1))
print(x)


