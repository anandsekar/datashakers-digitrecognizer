a-[]
a.append(1)
a.append(2)
distance=10

t=distance,a

results=[]
results.append(t)

# variables
number=10
string='vanakkam'
print number
print string
numberstring='100'
print int(numberstring)+100

#lists
list=[]
list.append('vanakkam')
list.append('world')
print list

for element in list:
	print element
	print 'vanakkam will print twice'
print 'only once'

map={}
map['anand']='sekar'
print map

tuple1='anand','sekar'
print tuple1[0]

class myclass:
	def sayvanakkam(self):
		print self.name

m=myclass()
m.name='anand sekar'
m.sayvanakkam()
n=myclass()
n.name='shyamalapriya'
n.sayvanakkam()

def passafunction():
	print "vanakkam"

def itakeafunction(functiontoexecute):
	functiontoexecute()

itakeafunction(passafunction)

