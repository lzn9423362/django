def heap_adjust(parent, heap):  # 更新结点后进行调整
    child = 2 * parent + 1
    while len(heap) > child:
        if child + 1 < len(heap):
            if heap[child + 1] < heap[child]:
                child += 1
        if heap[parent] <= heap[child]:
            break
        heap[parent], heap[child] = heap[child], heap[parent]
        parent, child = child, child * 2 + 1
def find(nums):
    print(len(nums))
    heapnum = len(nums) // 2
    heap = nums[:heapnum + 1]
    for i in range(len(heap) // 2 - 1, -1, -1):  # 前n/2个元素建堆
        heap_adjust(i, heap)
    for j in range(heapnum + 1, len(nums)):
        if nums[j] > heap[0]:
            heap[0] = nums[j]
            heap_adjust(0, heap)
            # 奇数时是最中间的数，偶数时是最中间两数的均值
    return heap[0] if len(nums) % 2 == 1 else float(heap[0] + min(heap[1], heap[2])) / 2
a = find([8, 9, 7, 54, 1, 321, 4, 7, 64, 13, 46, 7, 4, 613, 247, 87, 61, 32, 6, 876, 4, 1321,55])
print(a)