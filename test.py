#!/usr/bin/python
#coding:utf-8

from numpy import *
# frTrain = open('./Logistic/horseColicTraining.txt')
# trainingSet = []
# trainingLabels = []
# for line in frTrain.readlines():
# 	currLine = line.strip().split('\t')
# 	lineArr = []
# 	for i in range(21):
# 		lineArr.append(float(currLine[i]))
# 	trainingSet.append(lineArr)
# 	trainingSet.append(float(currLine[21]))
# print trainingSet

print zeros(3)

a = [1,2,3,4,'test']
c = [1,2,3,4,'test']
print a
b = [5,5]
print b
a.append(b)
print a
c.extend(b)
print c

del(a[0])
del(a[0])
print a

a = [1,2,4,6,9]
for i in a:
	print i
