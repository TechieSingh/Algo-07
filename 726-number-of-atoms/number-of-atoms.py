class Solution:
    def solve(self, i, s, n, prev_map):
        t = {}
        
        while i < n:
            if s[i] == '(':
                i = self.solve(i + 1, s, n, t)
            elif s[i].isupper():
                temp = s[i]
                i += 1
                
                if i < n and s[i].islower():
                    temp += s[i]
                    i += 1
                
                count = 0
                while i < n and s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
                
                t[temp] = t.get(temp, 0) + (count if count != 0 else 1)
                i -= 1
            elif s[i] == ')':
                i += 1
                count = 0
                while i < n and s[i].isdigit():
                    count = count * 10 + int(s[i])
                    i += 1
                
                if count > 0:
                    for key in t:
                        t[key] *= count
                    i -= 1
                
                for key in t:
                    prev_map[key] = prev_map.get(key, 0) + t[key]
                return i - 1
            i += 1
        
        for key in t:
            prev_map[key] = prev_map.get(key, 0) + t[key]
        return i

    def countOfAtoms(self, formula):
        n = len(formula)
        m = {}
        
        self.solve(0, formula, n, m)
        
        res = []
        for key in sorted(m.keys()):
            res.append(key)
            if m[key] != 1:
                res.append(str(m[key]))
        return ''.join(res)