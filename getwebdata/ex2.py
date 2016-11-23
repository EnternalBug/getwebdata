# try:
	# while 1:
		# a=input('input:')
		# c=int(a)
		# if c>1 and c<100:
			# print(c)
			# break
		# print("error")
# except ValueError:
	# print('please input numbers')
	
# b=0
# try:	
	# for i in range(5):
		# a=int(input('please input number'))
		# b=b+a
	# c=0
	# while c!='3':
		
		# c=input('please input change:\n1.sum\n2.arg\n3.exit')
		# if c=='1':
			# print(b)
		# if c=='2':
			# print(float(b)/5)
	
# except ValueError:
	# print('please input numbers')
# a=input('first:')
# b=input('second:')
# c=input('third:')
# if a>b:
	# if b>c:
		# print(a,b,c)
	# elif a>c:
		# print(a,c,b)
	# elif a<c:
		# print(c,a,b)
# if a<b:
	# if b>c:
		# if c>a:
			# print(b,c,a)
		# elif c<a:
			# print(b,a,c)
	# elif b<c:
		# print(c,b,a)
# import os
# ls=os.linesep
# while True:
    # choose=input('please input what are you want to do?\n1.write\n2.read\n3.exit')
    # if choose=='1':
        # name=input('please input file name')
        # if os.path.exists(name):
            # print("Are you want replace %s?\n"% name)
            # file=open(name,'r')
            # x=file.read()
            # file.close()              
            # print(x)
            # choose2=input('1.replace\n2.exit') 
            # if choose2=='1':
                # all=[]
                # while True:
                    # entry=input('please input words for lines,end for "."')
                    # if entry =='.':
                        # break
                    # else:
                        # all.append(entry)					
                # end=input('save?\n1.save\n2.exit')		 
                # if end=='1':		 
                    # file=open(name,'w')
                    # file.writelines(['%s%s'%(x,'\n') for x in all])	 
                    # file.close()		 
                # elif end=='2':
                    # continue				
        # continue
        # all=[]
        # while True:
            # entry=input('please input words for lines,end for "."')
            # if entry =='.':
                # break
            # else:
                # all.append(entry)
        # f=open(name,'w')
        # f.writelines(['%s%s'%(x,'\n') for x in all])
        # f.close()
        # print('Done!')
        # continue
    # elif choose=='2':
        # name=input('filename:')
        # try:
            # f=open(name,"r")
        # except FileNotFoundError as e:
            # print("file open error:",e)
        # for eachline in f:
            # print(eachline.strip('\r\n'))
        # f.close()
    # elif choose=='3':
        # exit()

# def chengji(a,b):
    # return a*b	
# a=input('please input first num:  ')
# b=input('please input second num:  ')	
# print(chengji(float(a),float(b)))

# def chengji(x):
    # if x>=90 and x<=100:
        # return "A"
    # elif x>=80:
        # return "B"
    # elif x>=70:
        # return "C"
    # elif x>=60:
        # return "D"
    # elif x<60:
        # return "F"
		
# sorce=input('please input your sorce:  ')
# print(chengji(int(sorce)))		


# def runnian(x):
    # if x%400==0:
        # return "Yes"
    # elif x%4==0:
        # if x%100!=0:
            # return "Yes"
        # else:
            # return "Not"
    # else:
        # return "Not"
# year=input('please input year:  ')
# print(runnian(int(year)))	

# def meifen(x):
    # one=0
    # five=0
    # ten=0
    # twentyfive=0
    # re={"25":0,"10":0,"5":0,"1":0}
    # twentyfive=x//25
    # ten=x%25//10
    # five=x%25%10//5
    # one=x%25%10%5;
    # re["25"]=twentyfive
    # re["10"]=ten
    # re["5"]=five
    # re["1"]=one;
    # return re	
# dollar=input('please input dollar:  ')
# print(meifen(int(float(dollar)*100)))	

# def bds(x):
    # if '+'in x:
        # re=x.split('+')
        # return float(re[0])+float(re[1])
    # elif '-' in x:
        # re=x.split('-')
        # return float(re[0])-float(re[1])
    # elif '**' in x:
        # re=x.split('**')
        # return float(re[0])**float(re[1])	
    # elif '/' in x:
        # re=x.split('/')
        # return float(re[0])/float(re[1])
    # elif '*' in x:
        # re=x.split('*')
        # return float(re[0])*float(re[1])
    # elif '%' in x:
        # re=x.split('%')
        # return int(re[0])%int(re[1])
# x=input('please input :  ')
# print(bds(x))	




# def money(a,b):
    # print("\t    Amount    Remaining\nPymt#\tPaid\tBalance\n")
    # print("-----\t------\t---------")
    # x=int(a/b)+2
    # n=0
    # m=0
    # while n!=x:
        # print("%d\t$%.2f\t$%.2f"%(n,m,a))
        # if a>b:
            # a=a-b;m=b;n=n+1
        # else:
            # m=a;a=0;n=n+1
        
    # return 0
	
# dollar=input('Enter opoening balance:  ')
# out=input('Enter monthly payment:  ')
# money(float(dollar),float(out))



# import random
# def ra():
    # ra1=0;ra2=ra3=[]
    # ra1=random.randint(1,100)
    # while ra1!=0:
        # ra2.append(random.randint(1,2**31-1))
        # ra1=ra1-1
        # x=1        
        # while x<10000:
            # x=x+1
    # ra1=random.randint(1,100)    		
    # while ra1!=0:
        # ra3.append(random.choice(ra2))
        # ra1=ra1-1
    # ra3.sort()
    # print(ra3)		
    # return 0
# ra()

# import keyword

# keyword=keyword.kwlist	
# global x
# x=input('num:')
# b=list(x)
# b.sort()
# b.reverse()
# print(b)		
		
# def chengji(a,b):
    # return a*b	
# a=input('please input first num:  ')
# b=input('please input second num:  ')	
# print(chengji(float(a),float(b)))

#6.4
# def chengji(x):
    # if x>=90 and x<=100:
        # return "A"
    # elif x>=80:
        # return "B"
    # elif x>=70:
        # return "C"
    # elif x>=60:
        # return "D"
    # elif x<60:
        # return "F"
		
		

# global x
# global n
# x=[]
# n=0
# for i in range(5):
    # sorce1=input('please input your sorce: ')
    # x.append(sorce1)
    # n=n+int(x[i-1])
# print(float(n)/5)

#6.5




# str1=input('input strings:')
# global x
# x=[]
# for i in str1:
#    x.append(i)
#
# op=input("please input the str's number:")
# n=0
# m=0
# while True:
#     if op.isdigit():
#         n=int(op)
#         print(x[n])
#     elif op == 'last':
#         n = n-1
#         print(x[n])
#     elif op == 'next':
#         n = n +1
#         print(x[n])
#     else:
#         break
#     op = input("please input the str's number:")

# str1=input('please input first string:')
# str2=input('please input second string:')
# x=len(str1)
# y=len(str2)
# if x<y: x=y
# for i in range(0,x):
#     if str1[i]==str2[i]:
#         continue
#     else:
#         print('False')
#         break

# str11=input('input string:')
# global n
# n=0
# for i in str11:
#
#     if n==0:
#         n+=1
#         continue
#     elif n==len(str11) and str11[n]!=str11[n-1] :
#         break
#     elif str11[n]==str11[n-1]:
#         print('double!')
#         break
#     n+=1
# str1=input('string:')
# d=len(str1)-2
# n=str1+str1[d::-1]
# print(n)
# 6.6
#
# str1=input('string:')
# b=''
# c=''
# state='start'
# state1='start'
# for i in str1:
#     if i==' ' and state=='start':
#         continue
#     else:
#         b=b+i
#         state='end'
# for i in b[::-1]:
#     if i==' ' and state1=='start':
#         continue
#     else:
#         c=c+i
#         state1='end'
# print(c[::-1])


# 6.7
# #!/usr/bin/env python
#
# # 标明PY执行文件路径
# num_str = input('Enter a Number: ')
# #让用户输入一个字符串(期望输入数字)
# num_num = int(num_str)
#
# #将用户输入转成数字
# fac_list = list(range(1,num_num+1))
# print ("BEFORE:",fac_list)
#
# #建立一个列表,内容为从1开始到用户输入的大小结束
# i=0
# j=0
# #定义变量i
# while i < len(fac_list):
#
#     #建立循环,循环次数为列表长度
#     if num_num % fac_list[i] ==0:
#          fac_list[i] ='x'
#          j=j+1
#         #筛掉可整除用户输入变量的数字
#     i = i + 1
#
# #变量i自增
#
# for n in range(0,j):
#     fac_list.remove('x')
#
# print("AFTER:",fac_list)

# 6.8

# x=input('input number(0-1000):')
# number=int(x)
# englishnumber=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty',]
# englishnumberten=['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','thousend']
#
# if number >=0 and number<21:
#     print(englishnumber[number])
# elif number >=0 and number<100:
#     print(englishnumberten[int(number/10)]+'-'+englishnumber[int(number-int(number/10)*10)])
# elif number >=0 and number==100:
#     print('one-hundred')
# elif number >=0 and number<121:
#     print(englishnumber[int(number/100)]+'-'+'hundred'+'-'+englishnumber[int(number-int(number/100)*100)])
# elif (number >=0 and number<1000 and (number-int(number/100)*100)<10):
#     print(englishnumber[int(number/100)]+'-'+'hundred'+'-'+englishnumber[int(number-int(number/10)*10)])
# elif number >=0 and number<1000:
#     print(englishnumber[int(number/100)]+'-'+'hundred'+'-'+englishnumberten[int((number-int(number/100)*100)/10)]+'-'+englishnumber[int(number-int(number/10)*10)])
# elif number >=0 and number==1000:
#     print('one-thousend')
# else:
#     print('out of limit')

# 6.9

# def minute(x):
#     if int(x/60)<24:
#         print(str(int(x/60))+':'+str(x-int(x/60)*60))
#     else:
#         print('out of limt')
# minutes=input('input minutes:')
# minute(int(minutes))

# 6.10

# word=input('input the word with big and small:')
#
# def wordupandlow(x):
#     op=list(x)
#     n=0
#     out=''
#     for i in op:
#         if i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
#             op[n]=i.upper()
#         elif i in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
#             op[n]=i.lower()
#         n=n+1
#     for m in op:
#         out=out+m
#     return out
#
# print(wordupandlow(word))

# 6.11
# ip= input('input the ip address:')
# number=ip.split('.')
# for i in number:
#     if int(i)>255:
#         print('out of limit')
#         break
# print(number)
# ip1=[]
# for n in range(0,4):
#     ip1.append(input('input the ip address:'))
#     if int(ip1[n])>255:
#         print('out of limit')
#         break
# if len(ip1) ==4:
#     print('.'.join(ip1))

# 6.12
#

# 6.13

# def atoc(string):
#     return complex(string)
#
# d=input('input complex:')
# print(atoc(d))

# 6.14
# import random
# rochambeau=['shitou','bu','jiandao']
# win=['shitou,jiandao','jiandao,bu','bu,shitou']
# while True:
#     x=input('input you choice:')
#     d=int(random.uniform(0,3))
#     result=rochambeau[d]+','+x
#
#     if result in win:
#         print(rochambeau[d],'computer is win')
#     elif x==rochambeau[d]:
#         print(rochambeau[d],'ping shou')
#     elif x=='exit':
#         break
#     else:
#         print(rochambeau[d],'you are win!')

# 6.15
# import datetime
# fm=input('input format:')
# # date=input('input date')
# # date2=input('input date2')
# brithday=input('input brithday')
# # x=date.split('/')
# # y=date2.split('/')
# z=brithday.split('/')
# next=datetime.datetime.today().year
# if fm=='MM/DD/YY':
#     # day=datetime.datetime(int(x[2]),int(x[0]),int(x[1]))
#     # day2 = datetime.datetime(int(y[2]), int(y[0]), int(y[1]))
#     bday = datetime.datetime(int(z[2]), int(z[0]), int(z[1]))
#     nextday = datetime.datetime( next, int(z[0]),int(z[1]))
# else:
#     # day = datetime.datetime(int(x[2]), int(x[1]), int(x[0]))
#     # day2 = datetime.datetime(int(y[2]), int(y[1]), int(y[0]))
#     bday = datetime.datetime(int(z[2]), int(z[1]), int(z[0]))
#     nextday = datetime.datetime( next, int(z[1]),int(z[0]))
#
#
#
# # print((day-day2).days)
# print((datetime.datetime.today()-bday).days)
# print((nextday-datetime.datetime.today()).days)

# 6.16
# M=[1,2,3,4,5]
# N=[6,7,8,9,10]
# x=[]
# y=[]
# for i in range(0,len(M)):
#     x.append(M[i]+N[i])
#     y.append(M[i]*N[i])
#
# print(x,y)

# 6.17
# def mypop(x):
#     n=len(x)
#     print(x[n-1])
#     y=x[:-1]
#     return y
# a=[1,2,3,4,5,6]
#
# b=mypop(a)
# print(b)

# 6.19

# import math
# a=list(input('please list:'))
# fm=input('please format(example:row/list,3):')
# b=fm.split(',')
# if b[0]=='row':
#     x=math.ceil(len(a)/int(b[1]))
#     n=0
#     t=0
#     m=0
#     for i in a:
#         print(i+'\t',end='')
#         n=n+1
#         if n%x==0 and m<int(b[1]) :
#             print('\n')
#             m=m+1
# if b[0]=='list':
#     x=math.ceil(len(a)/int(b[1]))
#     n=0
#     t=[]
#     for i in range(0,x):
#         t.append('')
#         for j in range(0,int(b[1])):
#             if i + j * x <len(a):
#                 #print(a[i + j * x] + '\t', end='')
#                 t[i]=t[i]+(a[i + j * x] + '\t')
#             else:
#                 #print('', end='')
#                 t[i] = t[i] +'\t'
#         #print('\n')
#         t[i]=t[i]+'\n'
#         n=n+1
#     for y in t:
#         print(y[::-1])

#example 7.2
# import time
# import hashlib
# import re
#
# db={}
# def newuser(name):
#
#     pwd=input('passwd:')
#     pwdcrypt=hashlib.sha1(pwd.encode('UTF-8')).hexdigest()
#     nowtime=time.strftime("%Y-%m-%d %X",time.localtime())
#     x={name:[pwdcrypt,nowtime]}
#     db.update(x)
# def olduser(name):
#
#         pwd = input('passwd:')
#         pwdcrypt = hashlib.sha1(pwd.encode('UTF-8')).hexdigest()
#         passwd = db[name][0]
#         lastlogintime = db[name][1]
#         nowtime = time.strftime("%Y-%m-%d %X", time.localtime())
#         if passwd == pwdcrypt:
#             if time.mktime(time.strptime(nowtime,'%Y-%m-%d %H:%M:%S'))-time.mktime(time.strptime(lastlogintime,'%Y-%m-%d %H:%M:%S'))<20:
#                 print("You already logged in at:",lastlogintime)
#                 db[name][1]=time.strftime("%Y-%m-%d %X",time.localtime())
#             else:
#                 print('welcome back',name,nowtime)
#         else:
#             print ('login incorrect')
#
# def login():
#     prompt = 'login desired:'
#     while True:
#         inname = input(prompt)
#         if re.match("^[0-9A-z]+$", inname):
#             pass
#         else:
#             print('error name')
#             continue
#         name = inname.lower()
#         if name in db.keys():
#             olduser(name)
#             break
#         else:
#             cho=input("You input a new name,do you wan't create a new user?\n Y/N")
#             if cho.lower()=='y':
#                 newuser(name)
#             else:
#                 continue
#
# def deleteuser():
#     name=input('delete user:').lower()
#     if name in db.keys():
#         pwd = input('passwd:')
#         pwdcrypt = hashlib.sha1(pwd.encode('UTF-8')).hexdigest()
#         passwd = db[name][0]
#         if passwd == pwdcrypt:
#             db.pop(name)
#             print('user is deleted')
#         else:
#             print ('passwd incorrect')
#     else:
#         print('user not exist')
# def listed():
#     print(db)
#
# def showmenu():
#     prompt ="""
# (N)ew User Login
# (E)xisting User Login
# l(O)gin
# (Q)uit
# (D)elete
# (L)isted
# Enter choice:"""
#     done = False
#     while not done:
#         chosen = False
#         while not chosen:
#             try:
#                 choice =input(prompt).strip()[0].lower()
#             except (EOFError, KeyboardInterrupt):
#                 choice = 'q'
#             print('\nYou picked:[%s]'%choice)
#             if choice not in'qdlo':
#                 print('invalid option,try again')
#             else:
#                 chosen =True
#         if choice == 'q': done= True
#         if choice == 'o': login()
#         if choice == 'e': olduser()
#         if choice == 'd': deleteuser()
#         if choice == 'l': listed()
# if __name__ =='__main__':
#     showmenu()



# 7.7
# b={}
# a={'1':'a','2':'b','3':'c'}
#
# for n in a.keys():
#     b[a[n]]=n
#
# print(b)

# 7.8
# x={}
# while True:
#     name=input('please input name:')
#     number=input('please input number')
#     x[name]=number
#     if name=='end':
#         break
# x.update([('test', '001'), ('good', '003'), ('end', '005'), ('dect', '002'), ('best', '004')])
# print(sorted(x.items(),key= lambda so:so[0],reverse= True))
# print(sorted(x.items(),key= lambda so:so[1],reverse= 1))

# 7.9

# def tr(srcstr,dststr,string,uporlow):
#     if uporlow==0:
#         string=string.lower()
#
#     str_n = 0
#     bx=0
#     chen = list(string)
#     dstlen=len(srcstr)
#     for x in string:
#         for y in srcstr:
#              if y==x:
#                  for n in range(0, dstlen):
#                      if str_n + n <len(string):
#                          if string[str_n + n] == srcstr[n]:
#                              bx+=1
#                          else:
#                              bx=0
#                              break
#                      if bx==len(dststr):
#                          for g in range(0,dstlen):
#                              chen[str_n + g]=dststr[g]
#                      else:
#                          continue
#         str_n += 1
#     return chen
#
# def dr(srcstr,dststr,string,uporlow):
#     if uporlow==0:
#         string=string.lower()
#         srcstr=srcstr.lower()
#
#     str_n = 0
#     bx=0
#     chen = list(string)
#     chea=list(srcstr)
#     srclen=len(srcstr)
#     dstlen=len(dststr)
#     for x in string:
#         for y in srcstr:
#              if y==x:
#                  bx=0
#                  for n in range(0, srclen):
#                      if str_n + n <len(string):
#                          if string[str_n + n] == srcstr[n]:
#                              bx+=1
#                          else:
#
#                              break
#                      if bx==len(srcstr):
#                          for g in range(0,dstlen):
#                              chen[str_n + g]=dststr[g]
#                          for h in range(dstlen,srclen):
#                              chen[str_n + h] = ''
#
#
#                      else:
#                          continue
#         str_n += 1
#     x=0
#     for i in chen:
#         if i=='':
#             x=x+1
#     for i in range(0,x):
#         chen.remove('')
#
#     return chen
# print(tr('Test','good','Testeesttest',1))
# print(dr('este','goo','Testeestest',0))

# 7.10

# def ro13(string):
#     string=list(string)
#     up=[]
#     low=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     for i in low:
#         up.append(i.upper())
#     str_n=0
#     for d in string:
#         bx=0
#         dx=0
#         for x in up:
#             if d==x:
#                 if (bx+13)<(26):
#                     string[str_n]=up[bx+13]
#                 else:
#                     string[str_n]=up[bx-13]
#
#
#             else:
#                 bx += 1
#                 continue
#
#
#         for x in low:
#             if d == x:
#                 if (bx + 13) < (26):
#                     string[str_n] = low[dx + 13]
#                 else:
#                     string[str_n] = low[dx - 13]
#
#             else:
#                 dx += 1
#                 continue
#
#         str_n+=1
#     a=''.join(string)
#     return a
#
# def ro31(string):
#     string=list(string)
#     up=[]
#     low=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     for i in low:
#         up.append(i.upper())
#     str_n=0
#     for d in string:
#         bx=0
#         dx=0
#         for x in up:
#             if d==x:
#                 if (bx+13)<(26):
#                     string[str_n]=up[bx-13]
#                 else:
#                     string[str_n]=up[bx+13]
#
#
#             else:
#                 bx += 1
#                 continue
#
#
#         for x in low:
#             if d == x:
#                 if (bx + 13) > (26):
#                     string[str_n] = low[dx - 13]
#                 else:
#                     string[str_n] = low[dx + 13]
#
#             else:
#                 dx += 1
#                 continue
#
#         str_n+=1
#     a=''.join(string)
#     return a
#
# x=input('please input your words:')
# print(ro31(x))
# print(ro13(x))
#
# 7.14
# import random
# def ra():
#     ra1=0
#     ra2=[]
#     ra3=[]
#     ra4=ra1=random.randint(1,10)
#
#     for a in range(0,ra1):
#         ra2.append(random.randint(0,9))
#         ra1=ra1-1
#         x=1
#         while x<10000:
#             x=x+1
#     ra1=random.randint(1,ra4)
#     for a in range(0, ra1):
#         ra3.append(random.choice(ra2))
#         ra1=ra1-1
#     ra3.sort()
#
#     return ra3
# a=set(ra())
# b=set(ra())
# print(a,b)
# g=0
# while g<3:
#     x=input('input a|b :')
#     y=input('input a&b :')
#     d=[]
#     c=[]
#     for i in x:
#         c.append(int(i))
#     for i in y:
#         d.append(int(i))
#     c=set(c)
#     d=set(d)
#     if (c ==a|b and d==a&b):
#         print(c)
#         print(d)
#         exit()
#     else:
#         print(c,d)
#         print('error')
#     g+=1
# print(a|b)

# 7.15
# a=set([1,2,3])
# b=set([3,4,5])
# print(a,b)
#
# x=input('please input:')
# if 'in' in x:
#     print(a in b)
# elif 'not' in x:
#     print(a not in b)

# 8.2
# f=int(input('input (f)rom:'))
# t=int(input('input (t)o:'))
# i=int(input('input (i)ncrement'))
# n=[]
# for o in range(f,t,i):
#     n.append(o)
#
# print(n)

# 8.3

# def isprimer(num):
#     count=int(num/2)
#     x=True
#     while count>1:
#         if num%count==0:
#             x=False
#             break
#         else:
#             count-=1
#
#     return x
# n=input('input number:')
# if int(n)==0 or int(n)==2 or int(n)==3:
#     print('True')
# else:
#     print(isprimer(int(n)))

# 8.4

# def getfactors(num):
#     count=int(num/2)
#     x=[]
#     while count >0:
#         if num%count ==0:
#             x.append(count)
#         count-=1
#     x.append(int(num))
#     return sorted(x)
# x=input('input number:')
# print(getfactors(int(x)))

# 8.5
# global x
# x=[]
# def syz(num):
#     count=int(num/2)
#     n=2
#     m=0
#     d=0
#
#     while n<count:
#         if num%n ==0 :
#             x.append(n)
#             m=num/n
#             d=1
#             break
#         n+=1
#     if m!=0:
#         syz(m)
#     if d!=1:
#         x.append(int(num))
#     return n
#
# number=input('input number:')
# syz(int(number))
# print(x)

# 8.6 找出完全数
# d=[]
# def getfactors(num):
#     count=int(num/2)
#     x=[]
#     while count >0:
#         if num%count ==0:
#             x.append(count)
#         count-=1
#     if sum(x)==num:
#         return 1
#     else:
#         return 0
# #x=input('input number:')
# for i in range(10000):
#     if getfactors(i)==1:
#         d.append(i)
# print(d)
# #print(getfactors(int(x)))

# 8.8
# def jc(num):
#     x=1
#     a=1
#     while a<=num:
#         x=x*a
#         a=a+1
#     return x
#
# d=input('number:')
# print(jc(int(d)))

# 8.9
# def fbnq(n):
#     i=1
#     g=1
#     m=0
#     for d in range(n):
#         m=i
#         i=g
#         g=i+m
#     return m
#
# print(fbnq(8))

# 8.12

# def lb(start,end):
#
#     if (start>33 and start<126) or (end>33 and end<126):
#         print('DEC','\t\t','BIN','\t\t','OCT','\t\t','HEX','\t\t','ASCII')
#         for i in range(start,end+1):
#             print(i,'\t\t',str(bin(i))[2:],'\t\t',str(oct(i))[2:],'\t\t',str(hex(i))[2:],'\t\t',chr(i))
#     else:
#         print('DEC','\t\t','BIN','\t\t','OCT','\t\t','HEX')
#         for i in range(start,end+1):
#             print(i,'\t\t',str(bin(i))[2:],'\t\t',str(oct(i))[2:],'\t\t',str(hex(i))[2:])
#
# a=input('请输入起始数字:')
# b=input('请输入结束数据:')
# lb(int(a),int(b))

# 9.1
# import os
#
# cwd=os.getcwd()
# filename=cwd+os.sep+('ex2.py')
# d=[]
# n=input('input rows number:')
# z=int(n)
# x=0
# f=open(filename,'r',encoding= 'UTF-8')
# for i in f:
#     if x<z:
#         print(i)
#     x+=1
# f.seek(0)
# g=f.readlines()
# print(len(g))

# 9.4

# import os
# import os.path
#
#
# cwd=os.getcwd()
# name=input('input file name:')
# filename=cwd+os.sep+name
# while True:
#     if os.path.isfile(filename):
#         break
#     else:
#         print('error name')
#
# x=1
# f=open(filename,'r',encoding= 'UTF-8')
# d=len(f.readlines())
# f.seek(0)
# for i in f:
#     print(i)
#     if x%25==0:
#         z = input('enter any key to continue')
#     elif x==d:
#         exit()
#     x+=1
#
#
# 9.5
# def chengji(x):
#     if x>=90 and x<=100:
#         return "A"
#     elif x>=80:
#         return "B"
#     elif x>=70:
#         return "C"
#     elif x>=60:
#         return "D"
#     elif x<60:
#         return "F"
#
# global x
# global n
# x=[]
# n=0
# f=open('chengji.txt','r',encoding='UTF-8')
# g=f.readlines()
# f.seek(0)
# for a in range(0,len(g)):
#     print(g[a].strip('\n'))
#
# for i in range(5):
#     x.append(g[i])
#     n=n+int(x[i-1])
# d=float(n)/5
# print(d)
# print(chengji(d))
#f.close()

# 9.6
# import os
# f1=open('111.txt','r',encoding='UTF-8')
# f2=open('222.txt','r',encoding='UTF-8')
# g=0
# while True:
#     d=f1.readline()
#     e=f2.readline()
#     if d!=e:
#         v=1
#         for x in range(0,len(d)):
#             if d[x]!=e[x]:
#                 print('row:', g)
#                 print('list:',v)
#                 print(d)
#                 print(e)
#                 break
#             v+=1
#
#         break
#     g+=1
# f1.close()
# f2.close()

# 9.7
# import os
# f=open('111.txt','r',encoding='UTF-8')
#
# for a  in f.readlines():
#     d=a.strip().split(' ')
#     x=''
#     if len(d)>2:
#         for i in range(2,len(d)):
#             x=x+(d[i])+' '
#
#         d[2]=x
#         print(d[0], d[1].split('/')[0], d[1].split('/')[1],d[2])
#     else:
#
#         print(d[0], d[1].split('/')[0], d[1].split('/')[1])

# 9.9
# import os
#
# path='C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35\\Lib'
# d=os.listdir(path)
# names=[]
# print(len(d))
# for i in range(0,len(d)):
#     if '.py' in d[i]:
#         names.append(d[i])
#
# for name in names:
#     x='C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\'+name
#     f=open(x,'r',encoding='UTF-8')
#     n=''
#     x=0
#     for a in f.readlines():
#         if '"""' in a.strip():
#             x+=1
#
#         if x>0:
#             n=n+a
#         if x==2:
#             print(name)
#             print(n)
#             break

#  9.11

# import os
#
# f=open('url.txt','r+',encoding='UTF-8')
#
# def newurl():
#
#     f.seek(0,2)
#     name=input('input URLName:')
#     url=input('input URLAddress:')
#     des=input('input URLDescription')
#     f.write(name+'|'+url+'|'+des+'\n')
#
#
#
# def alterurl():
#     f.seek(0)
#     for a in f.readlines():
#         l=a.strip().split('|')
#         print(l[0],'\t',l[1],'\t',l[2])
#     alurl=input('please select name:')
#     f.seek(0)
#     g = ''
#     for a in f.readlines():
#         l = a.strip().split('|')
#         if alurl ==l[0]:
#             url = input('input URLAddress:')
#             des = input('input URLDescription')
#             g=g+alurl+'|'+url+'|'+des+'\n'
#         else:
#             g=g+a
#
#     f.truncate()
#     f.seek(0)
#     f.write(g)
#
#
#
# def deleteurl():
#
#     f.seek(0)
#     l=[]
#     print('name\turl\tdescription')
#     for a in f.readlines():
#         l=a.strip().split('|')
#         print(l[0],'\t',l[1],'\t',l[2])
#     delurl=input('please select name:')
#     f.seek(0)
#     g = ''
#     for a in f.readlines():
#         l = a.strip().split('|')
#         if delurl !=l[0]:
#                 g=g+a
#
#     f.seek(0)
#     f.truncate()
#     f.write(g)
#     print(g)
#
# def selecturl():
#     f.seek(0)
#     n=1
#     seurl=input('please input strings:')
#     for a in f.readlines():
#         l=a.strip().split('|')
#         if seurl in l[0]or seurl in l[1]:
#             print(l)
#             n=0
#     if n==1:
#         print('Empty')
#
#
# def printurl():
#
#     f.seek(0)
#     l=[]
#     print('name\turl\tdescription')
#     for a in f.readlines():
#         l=a.strip().split('|')
#         print(l[0],'\t',l[1],'\t',l[2])
#
#
# def showmenu():
#     prompt ="""
# (N)ew URL
# (A)lter URL
# (D)elete URL
# (P)rint URL
# (S)elect
# (Q)uit
# Enter choice:"""
#     done = False
#     while not done:
#         chosen = False
#         while not chosen:
#             try:
#                 choice =input(prompt).strip()[0].lower()
#             except (EOFError, KeyboardInterrupt,IndexError):
#                 choice = 'q'
#             print('\nYou picked:[%s]'%choice)
#             if choice not in'qnadps':
#                 print('invalid option,try again')
#             else:
#                 chosen =True
#         if choice == 'q': done= True
#         if choice == 'a': alterurl()
#         if choice == 'n': newurl()
#         if choice == 'd': deleteurl()
#         if choice == 'p': printurl()
#         if choice == 's': selecturl()
#
# if __name__ =='__main__':
#     showmenu()
# f.close()
#
#

# 9.12
#9.9
import os
import re

path='E:\\GitHub\\getwebdata\\'
d=os.listdir(path)
names=['test.txt']



for name in names:
    x='E:\\GitHub\\getwebdata\\'+name
    f=open(x,'r',encoding='UTF-8')
    # n=''
    # x=0
    # y=0
    # for a in f.readlines():
    #     if '@command=N' in a.strip() or '@database_name=N'in a.strip():
    #         x+=1
    #
    #     if a[0]=="'":
    #         continue
    #     if x==1 and n=='':
    #         y+=1
    #         if a.strip("@command=N', \n\t")=='':
    #             y-=1
    #         else:
    #             n = n + str(y)+':'+a.strip("@command=N', \n\t") + '\n'
    #         continue
    #     if x>0 and x!=2:
    #         n=n+a.strip("', \n\t")+'\n'
    #     if x==2:
    #         print(n,end='')
    #         x=0
    #         n=''
    #         continue

    zz=re.compile("@command=N'[\s\S]*?@database")
    n=''
    for a in f.readlines():
        n=n+a
    g=zz.findall(n)
    y=0
    m=''
    for b in g:
        y=y+1
        m=str(y)+':'+b.replace('@command=N','').replace('@database','').strip("', \n\t")
        print(m)



