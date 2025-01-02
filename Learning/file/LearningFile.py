import json


# main
with open('Learning/File/flights.json', 'r') as f:
    data = json.load(f)

print(data)

'''
Flight Year Month

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
Yêu cầu: Đọc dữ liệu từ file JSON và in ra tổng số hành khách có chuyến bay trong năm x tháng y.

INPUT
Dòng đầu là số bộ Test.
Các dòng tiếp theo, mỗi dòng ghi năm x và tháng y.

OUTPUT
In tổng số hành khách.
Nếu không có hành khách nào được chở trong năm y tháng y thì in ra "Invalid".

Example
Input	        Output
2	
1959 May	    420
1940 January	Invalid

'''