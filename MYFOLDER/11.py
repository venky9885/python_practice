def rec(arr):
    print(arr)

    # print(tr)

    for i in range(len(arr)):

        # print(i)
        rec(arr[:i]+arr[i+1:])


print("*****************")
ar = [1, 2, 3]
rec(ar)

print("*****************")
for i in range(3):
    for j in range(i, 3):
        print(ar[j:])
# def subArraySum(arr):
#     n = len(arr)
#     sum = 0

#     # Pick a starting point
#     for i in range(n):
#         curr_sum = 0

#         print("rgdrgdrgrgr", arr[:i])
#         # try all subarrays starting with 'i'
#         for j in range(i, n):
#             print(arr[j:])

#             curr_sum += arr[j]
#             if (curr_sum == sum):
#                 print("Sum found between indexes", i, "and", j)
#                 return True

#     print("No subarray found")
#     return False


# # This code is contributed by phasing17
# # Driver program
# arr = [4, 3, 0, 1, -2, 6]

# print(subArraySum(arr))

# This code is Contributed by shreyanshi_arun.

# class Solution:
#     def __init__(self):
#         self.res = []

#     def permute(self, nums):
#         self.backtrack(nums, [])
#         return self.res

#     def backtrack(self, nums, path):
#         print(nums)
#         if not nums:
#             self.res.append(path)
#         for x in range(len(nums)):
#             # print(nums[x])
#             self.backtrack(nums[:x]+nums[x+1:], path+[nums[x]])
#         print("---------------------------------------")

# t = Solution()

# print(t.permute([1, 2, 3]))
