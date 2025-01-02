import json


#main
with open('Learning/File/tips.json', 'r') as f:
    data = json.load(f)

for _ in range(int(input())):
    sex, isSmoker = input().split()

    
    total_bills = [float(tip['total_bill']) for tip in data['tips'] if tip['sex'] == sex and tip['smoker'] == isSmoker]
    if len(total_bills) != 0:
        print(f"{sum(total_bills):.4f}", end=" ")
        print(f"{sum(total_bills) / len(total_bills):.4f}", end=" ")
        print(f"{min(total_bills):.4f}", end=" ")
        print(f"{max(total_bills):.4f}")

    else:
        print('No data found')
    

'''
Tips là dữ liệu về tiền bo (tips) cho nhà hàng bao gồm danh sách các từ điển cho mỗi bàn, bao gồm các trường:

"tips": [
    {
        "total_bill": "16.99",
        "tip": "1.01",
        "sex": "Female",
        "smoker": "No",
        "day": "Sun",
        "time": "Dinner",
        "size": "2"
    },
    {
        "total_bill": "10.34",
        "tip": "1.66",
        "sex": "Male",
        "smoker": "No",
        "day": "Sun",
        "time": "Dinner",
        "size": "2"
    }
]
Ý nghĩa các trường:
    total_bill:     Tổng số chi.
    tip:            Tiền bo.
    sex:            Giới tính (Male hoặc Female).
    smoker:         Hút thuốc hoặc không hút (Yes hoặc No).
    day:            Ngày trong tuần.
    time:           Buổi trong ngày (Dinner hoặc Lunch).
    size:           Số người có trên bàn ăn.

Yêu cầu:
Đọc từ file JSON và đưa ra các chỉ số thống kê (sum, avg, max, min) về tổng tiền hóa đơn (total_bill) theo yêu cầu đề bài.

Input:
Dòng đầu đưa vào số bộ test.
Lần lượt đưa vào giới tính và trạng thái hút thuốc.

Output:
Đưa ra 1 dòng gồm các chỉ số thống kê.
Các số thập phân lấy 4 chữ số sau dấu phẩy.


Ví dụ:
Input	    Output
1	
Male No	    1919.7500 19.7912 48.3300 7.5100
'''