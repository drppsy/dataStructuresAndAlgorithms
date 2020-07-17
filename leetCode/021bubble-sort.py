class Solutions:

    def bubbleSort(self,arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr


def test_solutions():
    s = Solutions()

    # arr1 = [2, 4, 7, 5, 8]
    # arr1 = s.bubbleSort(arr1)
    # print(arr1)

    arr2 = [6,654,32,34,1,2,8]
    arr2 = s.bubbleSort(arr2)
    print(arr2)


test_solutions()