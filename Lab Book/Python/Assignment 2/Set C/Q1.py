"""
Write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
"""


def binarySearch(arr, l, r, ele):
	if r >= l:
		mid = l + (r - l) // 2

		if arr[mid] == ele:
			return mid
		elif arr[mid] > ele:
			return binarySearch(arr, l, mid - 1, ele)
		else:
			return binarySearch(arr, mid + 1, r, ele)
	else:
		return -1


arr = [10, 20, 30, 40, 50]
ele = 40

result = binarySearch(arr, 0, len(arr)-1, ele)

if result != -1:
	print(f"Element {ele} is present at index {result}.")
else:
	print("Element is not present in array")