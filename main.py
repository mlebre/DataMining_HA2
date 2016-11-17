###########################################################
#                  Data Mining KTH
#   Homework 2: Frequent items and associating rules 
###########################################################

import sys


###########################################################
#                   Class defintion
###########################################################

class APriori:
	def __init__(self,name, k,sup_t):
		self.name=name
		self.s=sup_t # support threshold
		self.k=k # size of our maximal set
		self.processing=0 # number of times we applied the Apriori algo
		self.freq_subset=None
		self.set=None

	def pass1(self):
		''' Counting of self.processing-shingle thanks to the subset of size k-1
		'''
		fi=open(self.name, 'r')
		self.set=dict() # deletion of the previous set
		for line in fi:
			line=line.split(' ')
			line.remove('\n')
			if self.processing==0:
				self.firstProcess(line)
			else:
				self.process()
		self.processing+=1
		fi.close()
		

	def firstProcess(self, line):
		''' Application of first processing of Apriori alogirithm
		'''
		i=0
		while i+self.processing < len(line):
			if line[i] not in self.set.keys():
				# item not yet appear
				self.set[line[i]]=1
			else:
				self.set[line[i]]=self.set[line[i]]+1
			i+=1

	def process(self,line):
		i=0
		while i+self.processing<len(line):
			j=i+1
			while j+self.processing<len(line):
				if self.line[i:i+self.processing] and self.line[j:j+self.processing] in self.freq_subset:
					self.set[line] 
				j+=1
			i+=1


	def pass2(self):
		self.freq_subset=list()
		for i,e in enumerate(self.set.keys()):
			if float(self.set[e])/len(self.set)>=self.s:
				self.freq_subset.append(self.set.keys()[i])
				self.freq_subset.append(self.set[e])
		print self.freq_subset




###########################################################
#                Function defintion
###########################################################


				


###########################################################
#                      Main
###########################################################

file_name=sys.argv[1]
T=0.05

AP=APriori(file_name,2,T)
AP.pass1()
print 'Singleton search'
print AP.set
print 'Frequent item set'
print 'threshold:', AP.s
AP.pass2()
