def majority_element(nums):
    candidate, count = None, 0

    for num in nums:
        if count == 0:  # reset candidate!!
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate