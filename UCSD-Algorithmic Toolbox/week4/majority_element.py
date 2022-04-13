#python3
def majority_element(nums, lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element(nums,lo, mid)
            right = majority_element(nums,mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

def decision(nums, num):
  count = 0
  for i in nums:
    if i == num:
      count += 1
  if count >= len(nums)//2 +1:
    return 1
  else:
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    num = majority_element(input_elements, 0, input_n-1)
    print(decision(input_elements,num))
