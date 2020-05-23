class Solution:
    from collections import Counter
    def frequencySort(self, s: str) -> str:
        out = ''
        ordered_freq = Counter(s)
        
        for char,count in ordered_freq.most_common():
            out += char*count
        
        return out
                
        
