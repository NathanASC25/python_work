def find_left(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left+right) //2
        index = -1

        if nums[mid] == target:
            index = mid
            right = mid-1

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index

def find_right(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left+right)//2
        index = -1

        if nums[mid] == target:
            index = mid
            left = mid+1

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index

nums = [1, 3, 5, 5, 5, 7, 9]
target = 3

print(find_left(nums, target), find_right(nums, target))
