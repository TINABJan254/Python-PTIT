import json
import random

# Tạo dữ liệu giả
years = [str(year) for year in range(1940, 2025)]
months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

flights_data = {
    "flights": [
        {
            "year": random.choice(years),
            "month": random.choice(months),
            "passengers": str(random.randint(100, 2000))  # Số hành khách từ 100 đến 2000
        }
        for _ in range(500)  # Tạo 500 bản ghi
    ]
}

# Ghi vào file JSON
with open('Learning/File/flights.json', 'w') as f:
    json.dump(flights_data, f, indent=4)

print("File flights.json với dữ liệu giả đã được tạo thành công!")
