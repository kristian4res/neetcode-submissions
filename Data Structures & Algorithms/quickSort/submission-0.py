# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

def sort(arr: List[Pair], s: int, e: int):
    if (e - s + 1 <= 1):
        return arr

    pivot = arr[e]
    left = s

    for i in range(s, e):
        if (arr[i].key < pivot.key):
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left += 1
    
    temp = arr[left]
    arr[left] = arr[e]
    arr[e] = temp 

    sort(arr, s, left - 1)
    sort(arr, left + 1, e)

    return arr

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return sort(pairs, 0, len(pairs) - 1)
        
        