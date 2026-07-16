 n=len(s)

        for i in range(1,n-1):
            var=s[i:]+s[:i]
            if s==var:
                return True
        return False
        
