class mathDojo(object):

    def __init__(self):
        self.total = 0

    def add(self, *num):
        for i in range(0, len(num)):
			if type(num[i]) is list or type(num[i]) is tuple:
				for j in num[i]: 
					self.total += j
			else:
				self.total += num[i]
		# print self.total
        return self

    def subtract(self, *num): 
        for i in range(0, len(num)):
            if type(num[i]) is list or type(num[i]) is tuple:
                for j in num[i]: 
                    self.total -= j
            else:
                self.total -= num[i]
        return self

    '''def result(self):  #result is a definition, not a function. 
		print self.total
'''

print mathDojo().subtract(2).total
print mathDojo().add(2).add(2, 5).subtract(3, 2).total
print mathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).total

    
