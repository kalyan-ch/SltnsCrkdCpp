def heapifyUp(nums):
    ind = len(nums)-1
    par = (ind-1)/2

    while par >=0 and nums[par] < nums[ind]:
        #swap
        temp = nums[ind]
        nums[ind] = nums[par]
        nums[par] = temp

        ind = par
        par = (ind-1)/2

def extract_max(nums):
    ind = len(nums)
    if ind!=0:
        temp = nums[0]
        nums[0] = nums[ind-1]
        del nums[ind-1]
        heapifyDown(nums)

        return temp

def heapifyDown(nums):
    ind = 0
    lf = ind*2 + 1
    n = len(nums)

    while lf < n:
        bg = lf
        rt = ind*2 + 2
        if rt < n and nums[rt] > nums[lf]:
            bg = rt

        if nums[ind] > nums[bg]:
            break
        else:
            temp= nums[ind]
            nums[ind] = nums[bg]
            nums[bg] = temp

        ind = bg
        lf = ind*2 + 1


def kthLargestElement(nums, k):
    heap = []
    for x in nums:
        heap.append(x)
        heapifyUp(heap)
    num = 0
    for x in range(k):
        num = extract_max(heap)
    return num
