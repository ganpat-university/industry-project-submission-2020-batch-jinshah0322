def find_intersection(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)

    intersection = []

    for element in arr2:
        if element in arr1:
            intersection.append(element)
            arr1.remove(element)

    return intersection


array1 = [1, 2, 2, 1, 3, 4, 5]
array2 = [2, 2, 3, 6]

result = find_intersection(array1, array2)

print("Intersection of the two arrays:", result)