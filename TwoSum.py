# 题目：LeetCode 1. Two Sum
# 给定一个整数数组 nums 和一个目标值 target，找出和为 target 的两个整数的下标。
# 输入格式：
# 第一行：数组长度 n 和目标值 target
# 第二行：n 个整数，表示数组 nums
# 输出格式：
# 两个整数，表示下标 i 和 j（i < j）
def twoSum(nums, target):
    hash_map ={}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[nums[i]] = i
    return []
    
def main():
    n, target = map(int, input().split())
    nums = list(map(int, input().split()))

    result = twoSum(nums, target)
    if result:
        print(result[0], result[1])
    else:
        print("No solution found")
if __name__ == "__main__":
    main()
