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
			if line[i] not in self.set:
				# item not yet appear
				self.set.append(line[i])
				self.set.append(1)
			else:
				self.set[self.set.index(line[i])+1]=self.set[self.set.index(line[i])+1]+1
			i+=1

	def process(self,line):
		for i in xrange(len(line)-self.processing):
			add=True
			item1=list()
			for k in xrange(self.processing):
				item1.append(line[i+k])
			if str(item1).strip('[]\'') in self.freq_subset:
				for j in xrange(i+1,len(line)-self.processing):
					item2=list()
					for k in xrange(self.processing):
						item2.append(line[j+k])
					if str(item2).strip('[]\'') in self.freq_subset:
						item1=set(item1)
						item2=set(item2)
						if list(item1.union(item2)) not in self.set:
							self.set.append(list(item1.union(item2)))
							self.set.append(1)
						else:
							self.set[self.set.index(list(item1.union(item2)))+1]=self.set[self.set.index(list(item1.union(item2)))+1]+1					
				

	def pass2(self):
		self.freq_subset=list()
		i=0
		while i <len(self.set):
			if float(self.set[i+1])/(0.5*len(self.set))>=self.s: 
			# Dividing with self.process+1 because set contains the count of each item
				self.freq_subset.append(self.set[i])
			i+=2 # avoid the count of item



	def algoApplication(self):
		''' Application of the apriori algorithm to find the frequent items of length k
		'''
		print '\n--------------------------------'
		print 'Apriori algorithm to find subsets of length', self.k, 'with a threshold of', self.s, 'in file', self.name,'\n'
		for i in xrange(self.k):
			print 'Application number:', i
			self.pass1()
			self.pass2()
		print 'Frequent items with k members:'
		print self.freq_subset

###########################################################
#                Function defintion
###########################################################


				


###########################################################
#                      Main
###########################################################

file_name=sys.argv[1]
T=0.01

AP=APriori(file_name,2,T)
AP.algoApplication()