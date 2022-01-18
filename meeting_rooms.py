def meeting_rooms(arr):
    i = 0
    count = 1
    arr.sort(key=lambda x: x[0])
    print(arr)
    while i < len(arr) - 1:
        if arr[i+1][0] >= arr[i][0] and arr[i+1][0] <= arr[i][1] and arr[i+1][1] <= arr[i][1]:
            count += 1
        elif arr[i+1][0] <= arr[i][1]:
            count += 1
        else:
            count -= 1
        i += 1
    return count


print(meeting_rooms([
    [0, 14],
    [6, 25],
    [12, 19],
    [13, 19],
    [5, 9]
]))
