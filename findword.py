import sys

f = open('/Volumes/my_docs/Downloads/alt12dicts-4/test.txt' )
contents = f.readlines()
candidate=sys.argv[1]
print 'candidate: ' + candidate

result = []

for s in contents:
	failed = False
	s = s.replace('\r','')
	s = s.replace('\n','')
	cc = candidate

	for chr in s:
		pos = cc.find(chr)
		if pos < 0 : 
			failed = True
		else:
			cc = cc[:pos]+cc[pos+1:]
	if failed == False:
		result.insert(0,s)			
	
	
result.sort(lambda x,y: cmp(len(y) , len(x)))

for i in result:
	print i