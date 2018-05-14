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
	#print(B)
	NumA_2016 = np.zeros((len(data_2016), len(B)))
	NumA_2017 = np.zeros((len(data_2017), len(B)))
	NumA_2018 = np.zeros((len(data_2018), len(B)))
	NumA_2016 = json2numpy(B, data_2016, NumA_2016)
	NumA_2017 = json2numpy(B, data_2017, NumA_2017)
	NumA_2018 = json2numpy(B, data_2018, NumA_2018)
	print(NumA_2016)
#	print(NumA_1)
#print(ReadyElements_2016)


if __name__ == '__main__':
	main()
















