import csv
import operator
import numpy
import time
class Digit:
	def __init__(self):
		self.label=''
		self.data=[]

	def init(self):
		self.ndata=numpy.array(self.data)

	def distance(self,digit):
		return numpy.sum((self.ndata-digit.ndata)**2)**.5


def get_training_set():
	dataset=[]
	with open('../data/train.csv','rb') as csvfile:
		csvreader=csv.reader(csvfile)
		rownumber=0
		for row in csvreader:
			if not rownumber==0:
				data=Digit()
				dataset.append(data)
				colnumber=0
				for col in row:
					pixels=[]
					if colnumber==0:
						data.label=col
					else:
						data.data.append(int(col))
					colnumber=colnumber+1
				data.init()
			rownumber=rownumber+1
	return dataset
def get_test_set():
	dataset=[]
	with open('../data/test.csv','rb') as csvfile:
		csvreader=csv.reader(csvfile)
		rownumber=0
		for row in csvreader:
			if not rownumber==0:
				data=Digit()
				dataset.append(data)
				for col in row:
					data.data.append(int(col))
				data.init()
			rownumber=rownumber+1
	return dataset

trainingset=get_training_set()
testset=get_test_set()
f=open('./out1.csv','w')
f.write('ImageId,Label\n')
i=1
for test in testset:
	results=[]
	start=time.time()
	for train in trainingset:
		distance=test.distance(train)
		touple=distance,train
		results.append(touple)
	results=sorted(results,key=lambda result:result[0])
	labelmap={}
	for y in range(0,100):
		result=results[y]
		l=result[1].label
		if l in labelmap:
			labelmap[l]+=1
		else:
			labelmap[l]=1
	labelmap=sorted(labelmap.iteritems(),key=operator.itemgetter(1),reverse=True)
	f.write(str(i))
	f.write(',')
	f.write(labelmap[0][0])
	f.write('\n')
	print i
	print labelmap
	i=i+1
	end=time.time()
	print end-start
f.close()

	
