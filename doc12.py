# mark=[[8,3,4],[1,5,9],[6,7,2]]
# i=0
# while i<len(mark):
# 	j=0
# 	s=0
# 	sum=0
# 	while j<len(mark):
# 		sum=sum+mark[i][j]
# 		s=s+mark[i][j]
# 		j=j+1
# 	i=i+1
# 	print("row ",sum)
# 	print("cloums",s)
    
    
i=0
while i<=100:
    a=1
    c=0
    while a<=i:
        if i%2==0:
            c=c+1
        a=a+1
    if i==2:
        print(i,"prime no")
    i=i+1        