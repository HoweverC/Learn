class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        news = range(1, len(nums)+1)
        return list(set(news) - set(nums))