






import sys

def Symbol(Asm,Symbol_write):
	strr=[]
	for line in Asm.readlines():
		strr.append(line.split())
	#print(strr)
	dicti={"dd": 4 ,"db": 1 ,"resd": 4 ,"resb": 1}
	address=0
	arr=[]
	line_no=1
	sym_no=0
	Symbol_write.write("line_no"+"\t"+"Sym_no"+"\t"+"variable"+"\t"+"Address"+"\t"+"Section"+"\n")
	for i in strr:
		count=0
		if(len(i)>1):
			if 'dd' in i:
				a=i[0]
				b=address
				c=i[1]
				Symbol_write.write(str(line_no)+"\t"+str(sym_no)+"\t"+str(a)+"\t"+"\t"+str(b)+'\t'+str(c)+"\t"+"data_section"+'\n')
				for j in range(0,len(i[2])-1):
					if i[2][j]==',':
						count+=1
				address=address+(count*dicti['dd'])
			elif "db" in i:
				a=i[0]
				b=address
				c=i[1]
				Symbol_write.write(str(line_no)+"\t"+str(sym_no)+"\t"+str(a)+"\t"+"\t"+str(b)+'\t'+str(c)+"\t"+"data_section"+'\n')
				for j in range(0,len(i[2])-1):
					if ((i[2][j]!='"') and  (i[2][j]!=',') and (i[2][j]!='1') and (i[2][j]!='0')):
						count+=1
				address=address+(count*dicti['db'])
			elif "resd" in i:
				a=i[0]
				b=address
				c=i[1]
				Symbol_write.write(str(line_no)+"\t"+str(sym_no)+"\t"+str(a)+"\t"+"\t"+str(b)+'\t'+str(c)+"\t"+"bss_section"+'\n')
				address=address+(int(i[2])*dicti['resd'])
			elif "resb" in i:
				a=i[0]
				b=address
				c=i[1]
				Symbol_write.write(str(line_no)+"\t"+str(sym_no)+"\t"+str(a)+"\t"+"\t"+str(b)+'\t'+str(c)+"\t"+"bss_section"+'\n')
				address=address(int(i[2])*dicti['resb'])
			sym_no+=1
		line_no+=1		
	Symbol_write.close()



Asm=open(sys.argv[1],"r")
Symbol_write=open(sys.argv[2],"w")
Symbol(Asm,Symbol_write) 

