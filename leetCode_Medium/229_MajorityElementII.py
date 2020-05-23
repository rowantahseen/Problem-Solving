'''
**This solution aimes to be general and without mathematical calculations yet in  O(1) Space, O(n) Time**

According to a mathematical proof 
the (n/3) will give us 2 majority votes, 
but what happens if you faced n/2,n/4, n/5, n/6...n/k, don't know the mathematical proof of the number of candidates you will need exactly and yet you want to implement it in constant space O(constant)?

My solution is to use the denominater in (n/k) which is the k and set it as constant space to save k candidates and apply the same algorithm of Moore Majority Vote in the easy problem https://leetcode.com/problems/majority-element/

* if element is found in our map of candidates, we +1 its value (count)
* if there is room to add a new candidate (candidates number <  k ), we add it
* if our space is full and no room to add any new candidate we -1 all candidates
* we want to remove the candidates that have reached zero and keep only the candidates who are >= 1, therefore we create a temp_dict and then we make the old dict (candidates) = temp_dict
* At the end in linear time we go through the original array to count the number of times our suggest candidates appeared and check if they are > n//3

'''
class Solution:
	def majorityElement(self, nums: List[int]) -> List[int]:
		candidates = {}
		k = 3
		for num in nums:
			if num in candidates:
				candidates[num] += 1
			elif len(candidates) < k:
				candidates[num] = 1
			else:
				temp={}
				for c in candidates:
					candidates[c]-=1
					if candidates[c] >= 1:
						temp[c] = candidates[c]
				candidates = temp
		out = [k for k in candidates if nums.count(k) > len(nums) // 3]          
		return out
