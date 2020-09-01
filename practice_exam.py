# 3、反转整数：给定一个32位有符号整数，将整数中的整数进行反转
# eg：-321 -123
def reverse(str):
    if int(str) > 0:
        return int(str[::-1])
    if int(str) < 0:
        return -(int(str[-1:0:-1]))
print(reverse(str(-12222222222234)))

# # 2、最后一个单词的长度 ：eg：输入："Hello World" 输出：5
# def compute_length(str):
#     count = 0
#     for i in str[::-1]:
#         if i != ' ':
#             count += 1
#         elif i == ' ':
#             return count
# print(compute_length("hello world lxp"))
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
