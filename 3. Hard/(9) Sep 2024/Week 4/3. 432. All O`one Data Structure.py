class AllOne:
    # count={}
    # max_var = ""
    
    def __init__(self):
        self.count={}
        self.max_var = ""
        
    def inc(self, key: str) -> None:
        if key not in self.count:
            self.count[key] = 1
            if self.max_var == "":
                self.max_var = key
            return

        self.count[key] += 1
        if self.count[key] > self.count[self.max_var]:
            self.max_var = key

    def dec(self, key: str) -> None:
        self.count[key] -= 1
        # If the count of key is 0, remove it from the DS
        if self.count[key] == 0:
            del self.count[key]
            if key == self.max_var:
                self.max_var = ""
        else:
            if key == self.max_var:
                self.max_var = max(zip(self.count.values(), self.count.keys()))[1]

    def getMaxKey(self) -> str:
        return self.max_var

    def getMinKey(self) -> str:
        if not self.count:
            return ""

        return min(zip(self.count.values(), self.count.keys()))[1]