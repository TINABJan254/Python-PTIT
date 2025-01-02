import json
import random

# Tạo dữ liệu giả
def generate_fake_data(num_records):
    sexes = ["Male", "Female"]
    smoker_status = ["Yes", "No"]
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    times = ["Lunch", "Dinner"]

    fake_data = {
        "tips": [
            {
                "total_bill": f"{random.uniform(10, 100):.4f}",  # Tổng số chi từ 10 đến 100
                "tip": f"{random.uniform(1, 20):.2f}",  # Tiền bo từ 1 đến 20
                "sex": random.choice(sexes),
                "smoker": random.choice(smoker_status),
                "day": random.choice(days),
                "time": random.choice(times),
                "size": random.randint(1, 6)  # Số người từ 1 đến 6
            }
            for _ in range(num_records)
        ]
    }

    return fake_data

# Số lượng bản ghi
num_records = 500  # Bạn có thể thay đổi số lượng bản ghi ở đây

# Tạo dữ liệu
data = generate_fake_data(num_records)

# Ghi dữ liệu vào file JSON
with open("Learning/File/tips.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"File tips.json đã được tạo với {num_records} bản ghi!")
