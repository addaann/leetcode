from typing import List
import math
import unittest

"""
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

Example 1:
    Input: nums = [-4,-2,1,4,8]
    Output: 1
    Explanation:
        The distance from -4 to 0 is |-4| = 4.
        The distance from -2 to 0 is |-2| = 2.
        The distance from 1 to 0 is |1| = 1.
        The distance from 4 to 0 is |4| = 4.
        The distance from 8 to 0 is |8| = 8.
        Thus, the closest number to 0 in the array is 1.
    
Example 2:
    Input: nums = [2,-1,1]
    Output: 1
    Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:
    -   1 <= n <= 1000
    -   -105 <= nums[i] <= 105
"""

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest: int = nums[0]
        
        n_middle: int = math.ceil((len(nums) - 1) / 2)
        for i in range(1, n_middle + 1):
            left_side = nums[i]
            if abs(left_side) < abs(closest) or (abs(left_side) == abs(closest) and left_side > closest):
                closest = left_side
                
            right_side: int = nums[n_middle+i] if n_middle + i < len(nums) else None
            if right_side is not None:
                if abs(right_side) < abs(closest) or (abs(right_side) == abs(closest) and right_side > closest):
                    closest = right_side
        
        return closest
    
class Testu(unittest.TestCase):
    def test_closest_number_test(self):
        self.assertEqual(Solution().findClosestNumber([-4,-2,4,8,1]), 1)
        self.assertEqual(Solution().findClosestNumber([2,-1,1]), 1)
        self.assertEqual(Solution().findClosestNumber([-1,1]), 1)
        self.assertEqual(Solution().findClosestNumber([-22865,-8738,-74089,7874,63249,-60412,-19559,-27463,82166,7235,24878,24277,-52233,62885,17816,-70814,-56541,57127,-1195,-4114,24017,29766,98706,45524,-91459,74506,-37484,-6001,-97496,91182,64004,-64252,69945,54029,9739,-58133,81594,3221,-49836,12409,8668,66600,49614,57369,-26122,-29435,-69629,-73215,55637,-24225,-73940,48770,73211,-13812,84316,-33187,-56668,4776,33135,-73936,22847,-87178,-76382,-13900,-63366,-11405,3903,-97561,91264,42346,-53876,-46444,-60915,67747,-29950,40500,18242,-7628,42724,4287,-7956,-93301,-3093,52698,-87396,84906,10583,75335,-19956,10323,-76925,18473,73416,15898,27725,79218]), -1195)
        self.assertEqual(Solution().findClosestNumber([-15090,20341,-55819,49964,48409,92604,-90083,22694,46625,-50784,51945,-4414,6709,77016,9055,-85720,25189,-90879,90467,-11938,-82194,-98633,61886,-93147,-77165,-83682,96910,57837,-84996,11525,2734,-68480,83741,84414,76131,-47628,-16589,-47506,-8555,20115,-83144,98846,31645,-43897,39173,71072,64597,-46600,57285,2741,36188,-54121,89186,-44798,17928,-94864,-38480,8690,-87167,18597,-31064,-20276,-22354,65508,79671,-10349,-16127,-38308,58288,-47557,44461,10530,78339,-64326,-82262,-14001,-19472,69772,40091,-13423,60149,88146,75940,70328,-10805,-81628,82443,-93186,-54080,-82546,-37276,19341,7834,-59159,1569,-22411,-63358,-18345,1018,69192,-85090,96967,-88725,-48702,67324,-29869,-73431,-76826,31274,-96790,153,42252,-8592,-84898,-24501,81989,-83766,-81360,21483,-91930,21772,-70962,-92711,19401,-2859,-45445,49428,-38948,1686,-73264,36300,-21003,-9551,14158,-23495,62737,-14874,-85559,11605,-36203,53478,-60277,-29817,51290,21349,-6762,-10534,26912,32542,73095,-89446,1755,-29476,-43049,81027,26992,-16638,-11667,12248,-62665,33565,6129,20109,-93599,-69346,35442,14487,5524,-26868,-45590,66472,-26019,43932,23391,-16863,-56421,-1714,-83165,23587]), 153)