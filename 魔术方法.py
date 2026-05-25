class cu:
    def __init__(self,ct):
        self.ct=ct
    def __getitem__(self,cr):
        return self.ct[cr]
cc=cu(["a","b","c","d","e","f","g"])
for i in cc:
    print(i)
