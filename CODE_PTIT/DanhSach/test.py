res = [[x * y for x in range(1, 4)] for y in range(1, 3)]
#tương đương
# for y in range(1, 3):
#     tmp = []
#     for x in range(1, 4):
#         tmp.append(x * y)
#     res.append(tmp)
# [[1, 2, 3], [2, 4, 6]]

print(res)