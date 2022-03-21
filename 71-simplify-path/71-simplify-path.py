import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        output = []
        
        # if len(path) and path[-1] == '/':
        #     path = path[:-1]
        
        if len(path) and path[0] == '/':
            path = path[1:]
        
        dirs = re.split("//|/", path)
        
        for folder in dirs:
            if folder == '..' and output:
                output.pop()
            elif not folder or folder == '.' or folder == '..':
                continue
            else:
                output.append(folder)
        
        return '/' + '/'.join(output)
                