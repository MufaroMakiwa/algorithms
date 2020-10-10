import heapq


def sort_k_messed_array1(arr, k):
    heap = []
    sorted_array = []
    heapq.heapify(heap)

    for i in range(len(arr)):
        if i == len(arr) - 1:
            sorted_array.append(heapq.heappop(heap))
            break

        sorted_array.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i + 1])

    return sorted_array


def sort_k_messed_array(arr, k):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:

            start = i
            while arr[start] < arr[start - 1] and start > 0:
                arr[start], arr[start - 1] = arr[start - 1], arr[start]
                start -= 1

    return arr

if __name__ == '__main__':
    arr = [1, 0]
    print(sort_k_messed_array(arr, 2))