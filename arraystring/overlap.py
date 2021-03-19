class Solution:
   def solve(self, text, patterns):
      n = len(text)
      bold = [False] * n
      for i in range(n):
         for p in patterns:
            if text[i:].startswith(p):
               for j in range(len(p)):
                  bold[i + j] = True

      ans = ""
      for i in range(n):
        if bold[i] and (i == 0 or not bold[i - 1]):
            ans += "<b>"
        ans += text[i]
        if bold[i] and (i == n - 1 or not bold[i + 1]):
            ans += "</b>"
      return ans

ob = Solution()
text = "thisissampleline"
patterns = ["this", "ssam", "sample"]
print(ob.solve(text, patterns))

"""
>>> embolden_substrings('abcxyz', [])
'abcxyz'

>>> embolden_substrings('abcxyz', ['abc'])
'<b>abc</b>xyz'

>>> embolden_substrings('abcxyz123', ['abc', '123'])
'<b>abc</b>xyz<b>123</b>'

 >>> embolden_substrings('abcdxyz1234abc', ['abc', '123', 'bcd'])
 '<b>abcd</b>xyz<b>123</b>4<b>abc</b>'
"""


def embolden_substrings(mystr, substr):
    array_idx = [False] * len(mystr)
    for idx in range(len(mystr)):
        for text in substr:
            if mystr[idx:].startswith(text):
                for size in range(len(text)):
                    array_idx[idx + size] = True
                    
    result = ""
    bold_tag = "<b>"
    bold_end = "</b>"
    bold = False
    # bold_e = False
    for i , set_flag  in enumerate(array_idx):

        if set_flag:
            if not bold:
                result += bold_tag
                bold = True
                # bold_e = False
        else:
              if bold:  
            # if bold_e != True:
                result += bold_end
                # bold_e = True
                bold = False
            
            
        result += mystr[i]
    
    if bold:
        result += bold_end
    return result
   
            
            
            
        
print(embolden_substrings('abcxyz123', ['abc', '123']))
print(embolden_substrings('abcdxyz1234abc', ['abc', '123', 'bcd']))