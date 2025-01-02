import json

# main
with open('Learning/File/flights.json', 'r') as f:
    data = json.load(f)

print(len(data['flights']), len(data['flights'][0]))


'''
Đếm số dòng, số cột trong file flights.json
'''