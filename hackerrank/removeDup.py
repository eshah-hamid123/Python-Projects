def remove_duplicates(num_list):
    # new_arr = list(set(num_list))
    # return new_arr
    return [x for i, x in enumerate(num_list) if x not in num_list[:i]]


n = int(input())
final_lists = []
for i in range(n):
    nums = input()
    num_list = list(map(int, nums.split(' ')))
    distinct_list = remove_duplicates(num_list)
    final_array = distinct_list[:-1]
    final_lists.append(final_array)

for lst in final_lists:
    print(*lst)




