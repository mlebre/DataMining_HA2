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
		self.set=list() # deletion of the previous set
		for line in fi:
			line=line.split(' ')
			line.remove('\n')
			if self.processing==0:
				self.firstProcess(line)
			else:
				self.process(line)
		self.processing+=1
		fi.close()
		

	def firstProcess(self, line):
		''' Application of first processing of Apriori alogirithm
		'''
		i=0
		while i+self.processing < len(line):
			hashed=hash(line[i]) # we hash the item
			if hashed not in self.set:
				# item not yet appear
				self.set.append(hashed)
				self.set.append(1)
			else:
				self.set[self.set.index(hashed)+1]=self.set[self.set.index(hashed)+1]+1
			i+=1

	def process(self,line):
		print '\nPROCESS'
		for i in xrange(len(line)-self.processing):
			item1=line[i:i+self.processing]
			if str(item1).strip('[]\'') in self.freq_subset:				
				for j in xrange(i+1,len(line)-self.processing):
					item2=line[j:j+self.processing]
					#if str(item2).strip('[]\'') in self.freq_subset:
						#print item1, item2

				


	def pass2(self):
		self.freq_subset=list()
		i=0
		while i <len(self.set):
			if float(self.set[i+1])/(len(self.set)/(self.processing+1))>=self.s: 
			# Dividing with self.process+1 because set contains the count of each item
				self.freq_subset.append(self.set[i])
			i+=2




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
print AP.freq_subset
AP.pass1()
