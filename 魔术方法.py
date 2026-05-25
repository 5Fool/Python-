class cu:
    def __init__(self,ct):
        self.ct=ct
    def __getitem__(self,cr):
        return self.ct[cr]
cc=cu(["1","2","3","4","5","6","7","8"])
for i in cc:
    print(i)
