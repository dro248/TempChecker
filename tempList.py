

class TempList:
    l = list()
    
    def __init__(self, max_size):
	self.max_size = max_size
    
    def __str__(self):
	return str(self.l) 

    def append(self, item):
	self.l.append(item)
	if len(self.l) > self.max_size:
	    self.l.remove(self.l[0])
