
# # 1、两数之和：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数
# # 假设每个输入只对应一种答案，且同样的元素不能被重复利用

# Method 1
# def num_sum(num,target):
#     for i in range(len(num)):
#         for j in range(i+1,len(num-1)):
#             if target == num[i] + num[j]:
#                 yield [num[i],num[j]]
# print(type(num_sum([3,6,7,2],9)))
# print(list(num_sum([3,6,7,2],9)))
