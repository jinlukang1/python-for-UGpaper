#用于生成可以直接被keras读入的数组格式数据集
#基于python3

import numpy as np
import os
import json

#打开读取文件
with open(r'/Users/lukangjin/Documents/GitHub/python-for-UGpaper/heifei2016ready.json', 'rt',\
 encoding = 'utf-8') as fp1:
	text_2016 = fp1.read()
fp1.close()

with open(r'/Users/lukangjin/Documents/GitHub/python-for-UGpaper/heifei2017ready.json', 'rt',\
 encoding = 'utf-8') as fp2:
	text_2017 = fp2.read()
fp2.close()

with open(r'/Users/lukangjin/Documents/GitHub/python-for-UGpaper/heifei2018ready.json', 'rt',\
 encoding = 'utf-8') as fp3:
	text_2018 = fp3.read()
fp3.close()

data_2016 = json.loads(str(text_2016), strict = False)
data_2017 = json.loads(str(text_2017), strict = False)
data_2018 = json.loads(str(text_2018), strict = False)



#读取可以使用的要素
def GetReadyElements(data):
	#获取所有要素值
	paras = []
	for key in data[0]:
		paras.append(key)
	list_1 = []
	for i in range(paras.index('PRS'), paras.index('Q_PRS')):
		list_1.append(paras[i])
	return list_1

#对比两个数组取交集
def diff(listA, listB):
	retA = [i for i in listA if i in listB]
	return retA

#json格式转为numpy格式
def json2numpy(B, data, Num):
	for j in range(0, len(data)):
		for i in range(0, len(B)):
			Num[j][i] = float(data[j][B[i]])
	return Num

#生成可以直接使用的训练和测试数据
def GenTrainAndTest(B, nparr):
	Test = nparr[:, B.index('PRE_1h')]
	Train = np.delete(nparr, B.index('PRE_1h'), axis = 1)
	return Train, Test

#生成文件
def GennpyFile(num, A):
	f = open("/Users/lukangjin/Desktop/" + A, "wb")
	np.save(f, num)
	f.close()

#主函数
def main():
	ReadyElements_2016 = GetReadyElements(data_2016)
	print(len(ReadyElements_2016))
	ReadyElements_2017 = GetReadyElements(data_2017)
	print(len(ReadyElements_2017))
	ReadyElements_2018 = GetReadyElements(data_2018)
	print(len(ReadyElements_2018))
	A = diff(ReadyElements_2016, ReadyElements_2017)
	print(len(A))
	B = diff(ReadyElements_2018, A)
	print(len(B))
#	print(B)
	NumA_2016 = np.zeros((len(data_2016), len(B)))
	NumA_2017 = np.zeros((len(data_2017), len(B)))
	NumA_2018 = np.zeros((len(data_2018), len(B)))
	NumA_2016 = json2numpy(B, data_2016, NumA_2016)
	NumA_2017 = json2numpy(B, data_2017, NumA_2017)
	NumA_2018 = json2numpy(B, data_2018, NumA_2018)
	print(NumA_2016.shape)
#	print(B.index('PRE_1h'))
#print(ReadyElements_2016)
#	print(NumA_2016[:,21])
	Train_2016, Test_2016 = GenTrainAndTest(B, NumA_2016)
	Train_2017, Test_2017 = GenTrainAndTest(B, NumA_2017)
	Train_2018, Test_2018 = GenTrainAndTest(B, NumA_2018)
	print(Test_2018.shape, Train_2018.shape)

	GennpyFile(Train_2016, "Train_2016.npy")
	GennpyFile(Train_2017, "Train_2017.npy")
	GennpyFile(Train_2018, "Train_2018.npy")
	GennpyFile(Test_2016, "Test_2016.npy")
	GennpyFile(Test_2017, "Test_2017.npy")
	GennpyFile(Test_2018, "Test_2018.npy")

	f = open("/Users/lukangjin/Desktop/"+"Test_2018.npy", "rb")
	A = np.load(f)
	print(A)

if __name__ == '__main__':
	main()
















