#cd /Users/lukangjin/Desktop
#基于python3
''''elements':
'Station_Name,Datetime,Station_Id_d,Year,Mon,Day,Hour,PRS,PRS_Sea\
	,PRS_Change_3h,PRS_Change_24h,PRS_Max,PRS_Max_OTime,PRS_Min,PRS_Min_OTime,TEM\
	,TEM_Max,TEM_Max_OTime,TEM_Min,TEM_Min_OTime,TEM_ChANGE_24h,TEM_Max_24h,TEM_Min_24h\
	,DPT,RHU,RHU_Min,RHU_Min_OTIME,VAP,PRE_1h,PRE_3h,PRE_6h,PRE_12h,PRE_24h,PRE_Arti_Enc_CYC\
	,PRE,EVP_Big,WIN_D_Avg_2mi,WIN_S_Avg_2mi,WIN_D_Avg_10mi,WIN_S_Avg_10mi,WIN_D_S_Max\
	,WIN_S_Max,WIN_S_Max_OTime,WIN_D_INST,WIN_S_INST,WIN_D_INST_Max,WIN_S_Inst_Max\
	,WIN_S_INST_Max_OTime,WIN_D_Inst_Max_6h,WIN_S_Inst_Max_6h,WIN_D_Inst_Max_12h\
	,WIN_S_Inst_Max_12h,GST,GST_Max,GST_Max_Otime,GST_Min,GST_Min_OTime,GST_Min_12h\
	,GST_5cm,GST_10cm,GST_15cm,GST_20cm,GST_40Cm,GST_80cm,GST_160cm,GST_320cm,LGST\
	,LGST_Max,LGST_Max_OTime,LGST_Min,LGST_Min_OTime,VIS_HOR_1MI,VIS_HOR_10MI,VIS_Min\
	,VIS_Min_OTime,VIS,CLO_Cov,CLO_Cov_Low,CLO_COV_LM,CLO_Height_LoM,CLO_FOME_1,CLO_Fome_2\
	,CLO_Fome_3,CLO_Fome_4,CLO_FOME_5,CLO_FOME_6,CLO_FOME_7,CLO_Fome_8,CLO_Fome_Low\
	,CLO_FOME_MID,CLO_Fome_High,WEP_Now,WEP_Past_CYC,WEP_Past_1,WEP_Past_2,SCO\
	,Snow_Depth,Snow_PRS,FRS_1st_Top,FRS_1st_Bot,FRS_2nd_Top,FRS_2nd_Bot,Q_PRS,Q_PRS_Sea\
	,Q_PRS_Change_3h,Q_PRS_Change_24h,Q_PRS_Max,Q_PRS_Max_OTime,Q_PRS_Min,Q_PRS_Min_OTime\
	,Q_TEM,Q_TEM_Max,Q_TEM_Max_OTime,Q_TEM_Min,Q_TEM_Min_OTime,Q_TEM_ChANGE_24h,Q_TEM_Max_24h\
	,Q_TEM_Min_24h,Q_DPT,Q_RHU,Q_RHU_Min,Q_RHU_Min_OTIME,Q_VAP,Q_PRE_1h,Q_PRE_3h,Q_PRE_6h\
	,Q_PRE_12h,Q_PRE_24h,Q_PRE_Arti_Enc_CYC,Q_PRE,Q_EVP_Big,Q_WIN_D_Avg_2mi,Q_WIN_S_Avg_2mi\
	,Q_WIN_D_Avg_10mi,Q_WIN_S_Avg_10mi,Q_WIN_D_S_Max,Q_WIN_S_Max,Q_WIN_S_Max_OTime\
	,Q_WIN_D_INST,Q_WIN_S_INST,Q_WIN_D_INST_Max,Q_WIN_S_Inst_Max,Q_WIN_S_INST_Max_OTime\
	,Q_WIN_D_Inst_Max_6h,Q_WIN_S_Inst_Max_6h,Q_WIN_D_Inst_Max_12h,Q_WIN_S_Inst_Max_12h\
	,Q_GST,Q_GST_Max,Q_GST_Max_Otime,Q_GST_Min,Q_GST_Min_OTime,Q_GST_Min_12h,Q_GST_5cm\
	,Q_GST_10cm,Q_GST_15cm,Q_GST_20cm,Q_GST_40Cm,Q_GST_80cm,Q_GST_160cm,Q_GST_320cm\
	,Q_LGST,Q_LGST_Max,Q_LGST_Max_OTime,Q_LGST_Min,Q_LGST_Min_OTime,Q_VIS_HOR_1MI\
	,Q_VIS_HOR_10MI,Q_VIS_Min,Q_VIS_Min_OTime,Q_VIS,Q_CLO_Cov,Q_CLO_Cov_Low,Q_CLO_COV_LM\
	,Q_CLO_Height_LoM,Q_CLO_FOME_1,Q_CLO_Fome_2,Q_CLO_Fome_3,Q_CLO_Fome_4,Q_CLO_FOME_5\
	,Q_CLO_FOME_6,Q_CLO_FOME_7,Q_CLO_Fome_8,Q_CLO_Fome_Low,Q_CLO_FOME_MID,Q_CLO_Fome_High\
	,Q_WEP_Now,Q_WEP_Past_CYC,Q_WEP_Past_1,Q_WEP_Past_2,Q_SCO,Q_Snow_Depth,Q_Snow_PRS\
	,Q_FRS_1st_Top,Q_FRS_1st_Bot,Q_FRS_2nd_Top,Q_FRS_2nd_Bot'
'''

import matplotlib.pyplot as plt
import numpy as np
import json
import os

paras = ['Station_Name','Datetime','Station_Id_d','Year','Mon','Day','Hour','PRS','PRS_Sea'\
,'PRS_Change_3h','PRS_Change_24h','PRS_Max','PRS_Max_OTime','PRS_Min','PRS_Min_OTime','TEM'\
,'TEM_Max','TEM_Max_OTime','TEM_Min','TEM_Min_OTime','TEM_ChANGE_24h','TEM_Max_24h','TEM_Min_24h'\
,'DPT','RHU','RHU_Min','RHU_Min_OTIME','VAP','PRE_1h','PRE_3h','PRE_6h','PRE_12h','PRE_24h','PRE_Arti_Enc_CYC'\
,'PRE','EVP_Big','WIN_D_Avg_2mi','WIN_S_Avg_2mi','WIN_D_Avg_10mi','WIN_S_Avg_10mi','WIN_D_S_Max'\
,'WIN_S_Max','WIN_S_Max_OTime','WIN_D_INST','WIN_S_INST','WIN_D_INST_Max','WIN_S_Inst_Max'\
,'WIN_S_INST_Max_OTime','WIN_D_Inst_Max_6h','WIN_S_Inst_Max_6h','WIN_D_Inst_Max_12h'\
,'WIN_S_Inst_Max_12h','GST','GST_Max','GST_Max_Otime','GST_Min','GST_Min_OTime','GST_Min_12h'\
,'GST_5cm','GST_10cm','GST_15cm','GST_20cm','GST_40Cm','GST_80cm','GST_160cm','GST_320cm','LGST'\
,'LGST_Max','LGST_Max_OTime','LGST_Min','LGST_Min_OTime','VIS_HOR_1MI','VIS_HOR_10MI','VIS_Min'\
,'VIS_Min_OTime','VIS','CLO_Cov','CLO_Cov_Low','CLO_COV_LM','CLO_Height_LoM','CLO_FOME_1','CLO_Fome_2'\
,'CLO_Fome_3','CLO_Fome_4','CLO_FOME_5','CLO_FOME_6','CLO_FOME_7','CLO_Fome_8','CLO_Fome_Low'\
,'CLO_FOME_MID','CLO_Fome_High','WEP_Now','WEP_Past_CYC','WEP_Past_1','WEP_Past_2','SCO'\
,'Snow_Depth','Snow_PRS','FRS_1st_Top','FRS_1st_Bot','FRS_2nd_Top','FRS_2nd_Bot','Q_PRS','Q_PRS_Sea'\
,'Q_PRS_Change_3h','Q_PRS_Change_24h','Q_PRS_Max','Q_PRS_Max_OTime','Q_PRS_Min','Q_PRS_Min_OTime'\
,'Q_TEM','Q_TEM_Max','Q_TEM_Max_OTime','Q_TEM_Min','Q_TEM_Min_OTime','Q_TEM_ChANGE_24h','Q_TEM_Max_24h'\
,'Q_TEM_Min_24h','Q_DPT','Q_RHU','Q_RHU_Min','Q_RHU_Min_OTIME','Q_VAP','Q_PRE_1h','Q_PRE_3h','Q_PRE_6h'\
,'Q_PRE_12h','Q_PRE_24h','Q_PRE_Arti_Enc_CYC','Q_PRE','Q_EVP_Big','Q_WIN_D_Avg_2mi','Q_WIN_S_Avg_2mi'\
,'Q_WIN_D_Avg_10mi','Q_WIN_S_Avg_10mi','Q_WIN_D_S_Max','Q_WIN_S_Max','Q_WIN_S_Max_OTime'\
,'Q_WIN_D_INST','Q_WIN_S_INST','Q_WIN_D_INST_Max','Q_WIN_S_Inst_Max','Q_WIN_S_INST_Max_OTime'\
,'Q_WIN_D_Inst_Max_6h','Q_WIN_S_Inst_Max_6h','Q_WIN_D_Inst_Max_12h','Q_WIN_S_Inst_Max_12h'\
,'Q_GST','Q_GST_Max','Q_GST_Max_Otime','Q_GST_Min','Q_GST_Min_OTime','Q_GST_Min_12h','Q_GST_5cm'\
,'Q_GST_10cm','Q_GST_15cm','Q_GST_20cm','Q_GST_40Cm','Q_GST_80cm','Q_GST_160cm','Q_GST_320cm'\
,'Q_LGST','Q_LGST_Max','Q_LGST_Max_OTime','Q_LGST_Min','Q_LGST_Min_OTime','Q_VIS_HOR_1MI'\
,'Q_VIS_HOR_10MI','Q_VIS_Min','Q_VIS_Min_OTime','Q_VIS','Q_CLO_Cov','Q_CLO_Cov_Low','Q_CLO_COV_LM'\
,'Q_CLO_Height_LoM','Q_CLO_FOME_1','Q_CLO_Fome_2','Q_CLO_Fome_3','Q_CLO_Fome_4','Q_CLO_FOME_5'\
,'Q_CLO_FOME_6','Q_CLO_FOME_7','Q_CLO_Fome_8','Q_CLO_Fome_Low','Q_CLO_FOME_MID','Q_CLO_Fome_High'\
,'Q_WEP_Now','Q_WEP_Past_CYC','Q_WEP_Past_1','Q_WEP_Past_2','Q_SCO','Q_Snow_Depth','Q_Snow_PRS'\
,'Q_FRS_1st_Top','Q_FRS_1st_Bot','Q_FRS_2nd_Top','Q_FRS_2nd_Bot']

#打开读取文件
with open(r'/Users/lukangjin/Desktop/hefei20160401-20160901.txt', 'rt',\
 encoding = 'utf-8') as fp:
	data = fp.read()
fp.close()

#数据格式问题预处理
data = str(data).replace("\t","")


#将json格式转化为字典格式并读出
text = json.loads(str(data), strict = False)
Data = text['DS']

#-----------------------function define--------------------------#

#得到对应元素所有的值，返回一个列表
def get_elements(element, DS):
    list_1 = []
    for _ in range(len(DS)):
        list_1.append(DS[_][element])
    return list_1

#打印对应元素所有的值
def print_elements(element, DS):
    print(get_elements(element, DS),element)

#打印一个值在paras中的位置
def print_index(element, paras):
    print(paras.index(element))

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

#检验key是否存在于字典中，并打印
def TestKey(element, DS):
	if element in DS[1]:
		print(element)
	else:
		print('NaN')

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

#删除字典中的某个element,返回一个新的结构体
def DelElement(element, DS):
	DS_1 = DS
	for i in range (len(DS_1)):
		del DS_1[i][element]
	return DS_1

#记录不合格变量，返回一个列表
def GetTheFailedElement(DS, paras):
	list_3 = []
	for j in range(paras.index('Q_PRS'),len(paras)):
		if TestMissValue(paras[j], DS) > 10:
			list_3.append(paras[j])
	return list_3




#TestMissValue_all()

#先删除不合格要素的质控因子
TheQ_FailedElement = GetTheFailedElement(Data, paras)

for j in range(len(TheQ_FailedElement)):
	paras.remove(TheQ_FailedElement[j])

print(len(paras))

for i in range(len(TheQ_FailedElement)):
	NewElements1 = DelElement(TheQ_FailedElement[i], Data)

#再删除不合格要素
A = TheQ_FailedElement

for _ in range (len(A)):
	A[_] = str(A[_]).replace("Q_","")

TheFailedElement = A

for k in range(len(TheFailedElement)):	
	paras.remove(TheFailedElement[k])

print(len(paras))

for ii in range(len(TheFailedElement)):
	NewElements2 = DelElement(TheFailedElement[ii], NewElements1)

#print(NewElements2)
#测试新生产的合格数据
#TestMissValue_all(NewElements2, paras)

#保存新生成的合格数据
with open('heifei2016'+'.json','a') as outfile:  
    json.dump(NewElements2,outfile,ensure_ascii=False)  
    outfile.write('\n')

#print(len(NewElements))
#print(len(Newparas))
#TestMissValue_all(NewElements, Newparas)




#print(len(DS[0]), ' ', len(paras))

#TestKey('Q_PRS_Sea')
#for j in range(102, 197):
#    TestMissValue(paras[j])
#    print(' ')

#print_elements(paras[120])

#print_elements('Datetime')

#print(text)
#print(type(text))

#requestParams = text['requestParams']
#fieldNames = text['fieldNames']
#fieldUnits = text['fieldUnits']
#DS = text['DS']

#i = 3426
#the range of i is 0~3426

#print(DS[i])
#list_1 = ['0']
#for j in range(3427):
#    list_1.append(DS[j]['Datetime'])

#print(list_1)
#print(requestParams)
#print(fieldNames)
#print(fieldUnits)