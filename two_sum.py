from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key num,v:i
        map = {}
        for index, num in enumerate(nums):
            map[num] = index
        for i, n in enumerate(nums):
            j = map.get(target - n)
            if j is not None and i != j:
                return [i, j]

if __name__ == '__main__':
    t = TwoSum()
    nums = [1, 2, 3, 4, 5, 6]
    res = t.twoSum(nums, 9)
    print(res)
