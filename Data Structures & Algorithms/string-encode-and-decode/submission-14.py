class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if strs == ['']: return ''

        sizes = []

        strings = '#'

        encoded = ''

        for s in strs:

            sizes.append(len(s))
            strings += s

        for t in sizes:

            encoded += str(t) + ','
        
        encoded += strings

        return encoded

    def decode(self, s: str) -> List[str]:

        if s == '': return ['']

        decoded = []
        
        sizes = []

        word = ''

        curr_size = ''

        start = 0

        for j in range(len(s)):


            if s[j] == ',': 
                
                sizes.append(int(curr_size))
                
                curr_size = ''

                continue

            if s[j] == '#':
                
                start = j+1
                break

            curr_size += s[j]

        for p in sizes:

            for k in range(p):

                word += s[start]

                start += 1
            
            decoded.append(word)
            word = ''
        
        return decoded
