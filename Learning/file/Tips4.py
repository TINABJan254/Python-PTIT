import json


# main
with open('Learning/File/tips.json', 'r') as f: 
    data = json.load(f)

for _ in range(int(input())):
    day, time = input().split()

    total_tips = [float(tip['tip']) for tip in data['tips'] if tip['day'] == day and tip['time'] == time]

    if len(total_tips) != 0:
        print(f'{round(sum(total_tips)/len(total_tips), 4):.4f}')
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
Đọc từ file JSON và đưa ra trung bình tiền tip theo ngày và buổi trong ngày

Input:
Dòng đầu tiên đưa vào số bộ test.
Dòng thứ 2 ghi ngày và buổi trong ngày, cách nhau 1 khoảng trắng.

Output:
Đưa ra giá trị trung bình của tiền tip (tip).
Các giá trị thập phân cách nhau bởi 1 khoảng trắng.

Ví dụ:
Input	        Output
2	
Sun Dinner	    3.2251
Fri Break	    Invalid
'''