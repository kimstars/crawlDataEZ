import requests
import pandas as pd

name = []
toan = []
van = []
anh = []
SBD = []

id = 130000
for i in range(1, 385):
    try:
        id += 1
        link = "http://tracuudiem.thi.phutho.vn/Home/TraCuu?MaNhom=TS10%202024-2025&SoBD=" + str(id)
        res = requests.get(link)
        data = res.json()
        print(data)
        if(len(data) == 4):
            SBD.append(data[0]['Diem'])
            name.append(data[0]['TenMon'])
            van.append(data[1]['Diem'])
            toan.append(data[2]['Diem'])
            anh.append(data[3]['Diem'])

            print(id)
        # if (id > 130010) :
        #     break
    except Exception as e:
        print(f"Error at id {id}: {e}")
        break


# Tạo DataFrame và xuất ra file Excel
col0 = "SBD"
col1 = "Họ và tên"
col2 = "Toán"
col3 = "Văn"
col4 = "Anh"

print(len(SBD), len(name), len(toan), len(van), len(anh))

data = pd.DataFrame({col0: SBD, col1: name, col2: toan, col3: van, col4: anh})
data.to_excel('data2025.xlsx', sheet_name='sheet1', index=False)
