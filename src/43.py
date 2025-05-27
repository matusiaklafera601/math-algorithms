def find_max_subarray_sum(nums):
    max_current = nums[0]
    max_global = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
        else:
            max_current += nums[i]

        if max_current > max_global:
            max_global = max_current

    return max_global
