import requests
import pandas as pd

name = []
toan = []
van = []
anh = []

id = 130000
for i in range(1,442):
    try:
        id += 1
        link = "http://tracuudiem.thi.phutho.vn/Home/TraCuu?MaNhom=TS10%202022-2023&SoBD="+ str(id)
        res = requests.get(link)
        data = res.json()
        
        name.append(data[0]['TenMon'])
        toan.append(data[1]['Diem'])
        van.append(data[2]['Diem'])
        anh.append(data[3]['Diem'])

        
        print(id)
    except:
        pass

col1 = "Họ và tên"
col2 = "Toán"
col3 = "Văn"
col4 = "Anh"

data = pd.DataFrame({col1:name,col2:toan,col3:van,col4:anh})
data.to_excel('data.xlsx', sheet_name='sheet1', index=False)

