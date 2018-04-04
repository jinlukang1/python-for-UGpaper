'''
用于下载MUSIC上的数据资料
基于python3
'''

import requests
import os

Payload = {
	'userId':'BESZ_SJZ_QXT',
	'pwd':'123456',
	'interfaceId':'getSurfEleByTimeRangeAndStaID',
	'dataCode':'SURF_CHN_MUL_HOR',
	#以下是所需参数部分
	#具体参见http://10.48.89.55/cimissapiweb/apidataclassdefine_list.action
	'elements':'Station_Name,Cnty,Datetime,Station_Id_d,Year,Mon,Day,Hour,PRS',
	'timeRange':'(20170901000000,20170903060000)',
	'staIds':'54511',
	'orderBy':'Datetime:ASC',
	'dataFormat':'json'
}

url = 'http://10.48.89.55/cimiss-web/api'

r = requests.get(url, params = Payload)

#设置名称
data_file_name = 'test1'
data_dir_path = os.path.split(__file__)[0] + os.sep + 'data'
data_file_path = data_dir_path + os.sep + data_file_name

try:
	os.mkdir(data_dir_path)
except FileExistsError:
	pass

#写入文件
with open(data_file_path, mode = 'w', encoding = 'utf-8') as F :
	F.write(r.text)
