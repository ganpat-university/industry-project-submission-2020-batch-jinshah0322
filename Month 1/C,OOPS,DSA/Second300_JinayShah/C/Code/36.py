import math

def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def floyd_rivest_select(arr, left, right, k):
    while right > left:
        if right - left > 600:
            n = right - left + 1
            i = k - left + 1
            z = math.log(n)
            s = 0.5 * math.exp(2 * z / 3)
            sd = 0.5 * math.sqrt(z * s * (n - s) / n) * sign(i - n / 2)
            new_left = max(left, int(k - i * s / n + sd))
            new_right = min(right, int(k + (n - i) * s / n + sd))
            floyd_rivest_select(arr, new_left, new_right, k)
        t = arr[k]
        i = left
        j = right
        swap(arr, left, k)
        if arr[right] > t:
            swap(arr, left, right)
        while i < j:
            swap(arr, i, j)
            i += 1
            j -= 1
            while arr[i] < t:
                i += 1
            while arr[j] > t:
                j -= 1
        if arr[left] == t:
            swap(arr, left, j)
        else:
            j += 1
            swap(arr, right, j)
        if j <= k:
            left = j + 1
        if k <= j:
            right = j - 1
    return arr[k]

arr = [7, 3, 4, 0, 1, 6]
k = 2
res = floyd_rivest_select(arr, 0, len(arr) - 1, k - 1)
print(f'The {k}-th smallest element is {res}')