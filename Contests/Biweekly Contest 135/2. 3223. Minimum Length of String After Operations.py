class Solution:
    def minimumLength(self, s: str) -> int:
        # chr: [index]
        my_dict = {}
        for i, c in enumerate(s):
            if c in my_dict:
                my_dict[c].append(i)
            else:
                my_dict[c] = []
                my_dict[c].append(i)
        
        #print(my_dict)
        cnt = 0
        for key, value in my_dict.items():
            if len(value) >=3:
                if len(value) % 2 == 1:
                    cnt += len(value) - 1
                else:
                    cnt += len(value) - 1 - 1
            
        return len(s) - cnt