import csv


# main
with open('Learning/File/iris.csv', 'r') as f:
    csvreader = csv.DictReader(f)
    data = [row for row in csvreader]

for _ in range(int(input())):
    line = input().split()
    species, petal_length = line[0], float(line[1])

    sepal_lengths = [float(row['sepal_length']) for row in data if row['species'] == species and float(row['petal_length']) == petal_length]

    if len(sepal_lengths) != 0:
        print(f'{round(sum(sepal_lengths) / len(sepal_lengths), 4):.4f}')
    else: 
        print('Invalid')

'''
Iris_test

Dữ liệu về hoa được lưu trữ trong file "iris.csv" có cấu trúc như hình:

sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,setosa
4.9,3.0,1.4,0.2,setosa
4.7,3.2,1.3,0.2,setosa
5.0,3.6,1.4,0.2,setosa

Ý nghĩa các cột:
sepal_length: Chiều dài của đài hoa.
sepal_width: Chiều rộng của đài hoa.
petal_length: Chiều dài của cánh hoa.
petal_width: Chiều rộng của cánh hoa.
species: Tên loài hoa tương ứng (các loài: setosa, virginica, versicolor).

Viết chương trình đọc từ file CSV và in ra chiều dài trung bình của đài hoa (sepal_length) khi biết:

Tên loài (species).
Chiều dài trung bình của cánh hoa (petal_length) cho trước.

Input:
Dòng đầu là số bộ test.
Các dòng tiếp theo, mỗi dòng ghi ra tên loài và độ dài của cánh hoa (petal_length).

Output:
In ra trung bình của đài hoa (sepal_length). Lấy 4 chữ số thập phân sau dấu phẩy.
Nếu không tìm được giá trị nào thỏa mãn yêu cầu thì in ra "Invalid".

Ví dụ:
Input	        Output
2	
setosa          1.5	5.15
versicolor 7	Invalid
'''