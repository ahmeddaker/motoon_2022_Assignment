def smallestDiff(arr):
    arr.sort()
    return min(arr[i+1] - arr[i] for i in range(len(arr)-1))