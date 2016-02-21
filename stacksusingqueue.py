# code created y Rama Ganapathy , Amrita University , CBE , If there is any error or issue that you have found out ping me in 
# ramaganapathy96@outlook.com , follow me on github at github.com/ramaganpathy1
class queue:
	"s using q"
	def __init__(self):
		self.f=0 #size control var
		self.q=[0,0,0,0,0,0,0,0,0,0] #q array
	def eq(self,v):
		if(self.isEmpty !=False):
			self.q[self.f]=v #push operation using enqueue
			self.f=self.f+1
			return ""
		else:
			print "stack Full exception"
			return ""
	def deq(self): #pop operation using dequeue
		if(self.isEmpty != True):
			print self.q[0]
			for i in range(self.f-1):
				self.q[i]=self.q[i+1]
			self.q[self.f-1]="\0"
			self.f=self.f-1
			return ""
		else:
			print "stack empty exception"
			return ""
	def isEmpty(self):
		if(self.f !=0):
			return True
		else:
			return False
	def size(self):
		return self.f
def main(): #test function
	qq=queue()  #classobj
	for i in range(5):
		qq.eq(i)
	print qq.q
	print qq.isEmpty()
	print "Size:" . qq.size()
	for i in range(5):
		qq.deq()
	print qq.q
	
	print "Size" . qq.size()
	print qq.isEmpty()
	return ""
main()