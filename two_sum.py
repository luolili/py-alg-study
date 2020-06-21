from typing import List


class TwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in map:
                return [map[num], index]
            else:
                map[num] = index
        return None
