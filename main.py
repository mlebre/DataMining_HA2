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
		self.freq_subset=list()
		self.set=dict()

	def pass1(self, freq_subsets=list()):
		''' Filtering of self.processing-shingle thanks to the subset of size k-1
		'''
		fi=open(self.name, 'r')
		self.set=dict() # deletion of the previous set
		for line in fi:
			line=line.split(' ')
			line.remove('\n')
			if self.processing==0:
				self.firstProcess(line)
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





###########################################################
#                Function defintion
###########################################################


				


###########################################################
#                      Main
###########################################################

file_name=sys.argv[1]
T=0.01

AP=APriori(file_name,2,T)
AP.pass1()
print 'Singleton search'
print AP.set
