#用于优化细处理第一次处理后的数据
import os
import json

#打开读取文件
with open(r'/Users/lukangjin/Desktop/heifei2018.json', 'rt',\
 encoding = 'utf-8') as fp:
	text = fp.read()
fp.close()

data = json.loads(str(text), strict = False)

#得到对应元素所有的值，返回一个列表
def get_elements(element, DS):
    list_1 = []
    for _ in range(len(DS)):
        list_1.append(DS[_][element])
    return list_1

#打印对应元素所有的值
def print_elements(element, DS):
    print(get_elements(element, DS),element)

#检验一个变量的缺省数量
def TestMissValue(element, DS):
    count = 0
    
    list_2 = get_elements(element, DS)

    for i in range(len(list_2)):
        if list_2[i] == '0':
            count = count
        elif list_2[i] == '3':
            count = count
        elif list_2[i] == '4':
            count = count
        else:
            count = count + 1
    
    return count

#打印测试后的缺省值占总数的比例
def print_TestMissValue(element, DS):
    print(TestMissValue(element, DS),'/', len(DS), element)

#计算变量总体的不合格数
def TestMissValue_all(DS, paras):
    count_all = 0
    for j in range(paras.index('Q_PRS'), len(paras)):
        print_TestMissValue(paras[j], DS)
        if TestMissValue(paras[j], DS) > 5:
            count_all = count_all + 1
        else:
        	count_all = count_all
        print('\n')
    print(count_all)

#通过质检码找到缺省值位置
def FindFailedQ_Value(element, DS):
	
    list_3 = get_elements(element, DS)

    list_4 = []

    for i in range(len(list_3)):
        if list_3[i] == '0':
            True
        elif list_3[i] == '3':
            True
        elif list_3[i] == '4':
            True
        else:
            list_4.append(i)
#            list_4.append(DS[i][element])

    return list_4

#查找并输出缺省值
def FindFailedValue(element, paras, DS):
	Num = FindFailedQ_Value(element, DS)
	A = paras.index('Q_PRS') - paras.index('PRS') 
	NoQElement = paras[paras.index(element) - A]
	for i in Num:
		print(i)
		print(DS[i-1][NoQElement], DS[i][NoQElement], DS[i+1][NoQElement])

def GetFailedData(element, paras, DS):
	Num = FindFailedQ_Value(element, DS)
	A = paras.index('Q_PRS') - paras.index('PRS') 
	NoQElement = paras[paras.index(element) - A]
	return Num, NoQElement


#将所有元素在列表中排序
paras = []
for key in data[0]:
	paras.append(key)

#for i in range(paras.index('Q_PRS'), len(paras)):
#	Num, NoQElement = GetFailedData(paras[i], paras, data)
#	for j in Num:
#		data[j][NoQElement] = data[j+1][NoQElement]
#	FindFailedValue(paras[i], paras, data)

for i in range(paras.index('Q_PRS'), len(paras)):
	Num, NoQElement = GetFailedData(paras[i], paras, data)
	for j in Num:
		data[j][NoQElement] = data[j-1][NoQElement]
	FindFailedValue(paras[i], paras, data)

ReadyData = data

with open('heifei2018ready'+'.json','a') as outfile:  
    json.dump(ReadyData,outfile,ensure_ascii=False)  
    outfile.write('\n')
#for i in range(paras.index('Q_PRS'), len(paras)):
#	Num, NoQElement = GetFailedData(paras[i], paras, data)
#	for j in Num:
#		data[j][NoQElement] = data[j+1][NoQElement]
#	FindFailedValue(paras[i], paras, data)
#TestMissValue_all(data, paras)
#print(FindFailedQ_Value('Q_PRS_Sea', data))
#FindFailedValue('Q_PRS_Sea', paras, data)

#print(paras)
#print_elements('PRS', data)