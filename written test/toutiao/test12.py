import sys

def lengthOfLongestSubstring(s):        
  hash_table = {}
  max_len = -1
  cur_left = 0
         
  for i, c in enumerate(s):
      print(i,c)
      if c in hash_table and hash_table[c] >= cur_left:
          cur_left = hash_table[c] + 1
      else:
          max_len = max(max_len, i - cur_left + 1)
      hash_table[c] = i
  return max_len

if __name__=="__main__":
  line=sys.stdin.readline().strip()
  res=lengthOfLongestSubstring(line)
  print(res)