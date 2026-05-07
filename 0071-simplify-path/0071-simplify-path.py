class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split the path by "/"
        parts = path.split("/")
        
        for part in parts:
            # Ignore empty parts and current directory "."
            if part == "" or part == ".":
                continue
            
            # Go back to parent directory
            elif part == "..":
                if stack:
                    stack.pop()
            
            # Valid directory name
            else:
                stack.append(part)
        
        # Build the canonical path
        return "/" + "/".join(stack)
        