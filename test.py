import requests
import csv

row = []

id = 130000
for i in range(1,441):
    id += 1
    link = "http://tracuudiem.thi.phutho.vn/Home/TraCuu?MaNhom=TS10%202021-2022&SoBD="+ str(id)
    res = requests.get(link)
    data = res.json()
    line = ""
    line = data[0]['TenMon'] + "," + data[1]['Diem']   + "," +  data[2]['Diem']   + "," + data[3]['Diem']
    row.append(line)
    print(id)


fields = 'Họ và tên,Toán,Văn,Anh' 

with open("temp.csv", mode = "w", encoding="utf-8") as f:
    f.write(fields)
    for r in row:
        f.write("\n")
        f.write(r)
