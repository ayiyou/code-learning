list = [1, 2, 3, 4, 5, 7, 6, 3, 2, 3, 8]
# for i in list:
#     for j in list[i+1:]:
#         if i == j:
#             list.pop(j)
# print(list)


duplicate_nums = []
for i in list:
    i_show_count = list.count(i)
    if i_show_count > 1 and [i, i_show_count] not in duplicate_nums:
        duplicate_nums.append([i, i_show_count])

print(duplicate_nums)

for item in duplicate_nums:
    duplicate_n = item[0]
    duplicate_times =item[1]
    for j in range(duplicate_times-1):
        list.remove(duplicate_n)
print(list)


