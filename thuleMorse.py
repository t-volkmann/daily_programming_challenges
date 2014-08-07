#!/usr/bin/python
count = 0
MAX_ITERATIONS = 6

def thuleMorse( a ):
	b = list(a);
	global count

	if count == 0:
		print "%s : %s" % (count, a)
		count = count + 1
		return thuleMorse(a);

	while count < MAX_ITERATIONS:
		for x in b:
			if b[x] == 0:
				b[x] = 1
			else:
				b[x] = 0

		c = a + b
		
		try:
			print"%s : %s"%(count , c)
			count = count + 1
			return thuleMorse(c)
		except RuntimeError:
			print "Oppsies!"
		
	
def main():
	l = [0];
	thuleMorse(l)

if __name__ == "__main__":
	main()
