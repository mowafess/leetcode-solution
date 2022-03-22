import re

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        stack = []
        res = 0

        for entry in input.splitlines():
            name, depth = entry.lstrip('\t'), entry.count("\t")
            
            # go back up to the folder before the depth
            # we need to use = cos we dont also want files or folders in
            # them same parent folder concating names
            
            while stack and stack[-1][1] >= depth:
                stack.pop()
                
            prefix = stack[-1][0]+'/' if stack else ""                
            stack.append((prefix+name, depth))

            # if we have a file, update maximum length
            if stack and '.' in stack[-1][0]:
                res = max(res, len(stack[-1][0]))

        return res
        
        
#     Not working
#         tabs = 0
#         expr = '\t'
#         output = 0
        
#         def dfs(path_string, others, tabs):
#             if expr not in others:
#                 if '.' in others:  
#                     output = max(len(path_string + others), output)
#                 return
            
#             tabs += 1
        
#             subdir = re.split(r'\n\t{}'.format(tabs), others)
#             print(subdir)
            
#             root = path_string + subdir[0] + '/'
            
#             for subs in subdir[1:]:
#                 dfs(root, subs, tabs)
                
        
#         dfs('', input, 0)
        
#         return output