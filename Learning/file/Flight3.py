import json

# main
with open('Learning/File/flights.json', 'r') as f:
    data = json.load(f)

for _ in range(int(input())):
    start_year, end_year = map(int, input().split())

    passengers = [int(flight['passengers']) for flight in data['flights'] if int(flight['year']) >= start_year and int(flight['year']) <= end_year]

    if len(passengers) == 0:
        print('Invalid')
    else:
        print(sum(passengers))

'''
Dữ liệu về chuyến bay được lưu trữ trong tệp "flights.json" có cấu trúc từ điển lồng nhau bao gồm:

Ngoài cùng là từ điển có khóa là flights.
Giá trị của khóa là danh sách các từ điển, mỗi phần tử bao gồm các khóa và giá trị text như hình:


{
  "flights": [
    {
      "year": "1949",
      "month": "January",
      "passengers": "112"
    },
    {
      "year": "1949",
      "month": "February",
      "passengers": "118"
    },
    {
      "year": "1949",
      "month": "March",
      "passengers": "132"
    }
  ]
}
Trong đó:

Giá trị của khóa year là năm thống kê.
Giá trị của khóa month là tháng thống kê.
Giá trị của khóa passengers là số hành khách chở được tương ứng.
Yêu cầu: Đọc dữ liệu từ file JSON và in ra tổng số hành khách từ năm x đến năm thứ y.

INPUT:
Dòng đầu là số bộ Test.
Các dòng tiếp theo, mỗi dòng ghi 2 năm x và y, đảm bảo x < y.
OUTPUT:
In ra tổng số hành khách từ năm x đến năm thứ y.
In tổng số hành khách theo từng dòng. 
Nếu không có hành khách nào được chở từ năm x đến năm y, in ra "Invalid".

Input	Output
2	
1949 1950	1520
1939 1942	Invalid
'''