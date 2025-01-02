import json



# main
with open('Learning/File/flights.json', 'r') as f:
    data = json.load(f)

for _ in range(int(input())):
    line =  input().split()
    year, statistic = line[0], line[1]

    passengers = [int(flight['passengers']) for flight in data['flights'] if flight['year'] == year]

    if len(passengers) != 0:
        if statistic == 'sum':
            print(sum(passengers))
        elif statistic == 'min':
            print(min(passengers))
        elif statistic == 'max':
            print(max(passengers))
        elif statistic == 'avg':
            print(f'{round(sum(passengers) / len(passengers), 5):.4f}')
    else:
        print('No data found')



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
    }
  ]
}

Trong đó:

Giá trị của khóa year là năm thống kê.
Giá trị của khóa month là tháng thống kê.
Giá trị của khóa passengers là số hành khách chở được tương ứng.
Yêu cầu: Đọc dữ liệu từ file JSON và in ra các thông tin thống kê theo năm.

INPUT:
Dòng đầu là số bộ Test.
Các dòng tiếp theo, mỗi dòng ghi số năm và chỉ số cần thống kê (min, max, sum, avg).
OUTPUT
In ra giá trị tính được. Nếu giá trị là dạng float thì in ra làm tròn đến 5 chữ số sau dấu phẩy.

Example
Input	    Output
2	
1959 sum	5140
1950 avg	139.66667
'''