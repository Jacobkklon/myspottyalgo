    def romanToInt(self, s):
        #Cases are I, V, X, L, C, D, M
        result = 0
        for i in s:
            if i == 'I':
                val = 1
            if i == 'V':
                val = 5
            if i == 'X':
                val = 50
            if i == 'L':
                val = 100
            if i == 'D':
                val = 500
            if i == 'M':
                val = 1000
            result += val
            return(result)
romantoInt('III')