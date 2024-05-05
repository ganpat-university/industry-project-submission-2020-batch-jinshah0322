def find_median_sorted_arrays(nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < len(nums1):
        merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    total_length = len(merged)
    mid = total_length // 2

    if total_length % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]

nums1 = [1, 3]
nums2 = [2]

median = find_median_sorted_arrays(nums1, nums2)
print(f"The median is: {median}")