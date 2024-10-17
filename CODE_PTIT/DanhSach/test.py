def merge(a, L, mid, R):
    v1 = a[L:mid + 1]
    v2 = a[mid + 1:R + 1]

    i, j = 0, 0
    cnt = 0
    while i < len(v1) and j < len(v2):
        if v1[i] <= v2[j]:
            a[L] = v1[i]
            i += 1
        else:
            a[L] = v2[j]
            j += 1
            cnt += len(v1) - i  # Count inversions
        L += 1

    while i < len(v1):
        a[L] = v1[i]
        i += 1
        L += 1
    while j < len(v2):
        a[L] = v2[j]
        j += 1
        L += 1

    return cnt

def merge_sort(a, L, R):
    if L < R:
        mid = (L + R) // 2
        res = 0
        res += merge_sort(a, L, mid)
        res += merge_sort(a, mid + 1, R)
        res += merge(a, L, mid, R)
        return res
    return 0   

if __name__ == "__main__":
    print('hello hello world')