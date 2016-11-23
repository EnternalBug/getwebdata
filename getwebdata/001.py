##导出SQL任务计划相关动作,需要生成作业脚本作为数据来源

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
