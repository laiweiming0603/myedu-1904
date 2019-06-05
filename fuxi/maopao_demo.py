alist=[8,5,4,9,3,7,1,2,6]
def maopao():

    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]>alist[j+1]:
                temp=alist[j]
                alist[j]=alist[j+1]
                alist[j+1]=temp
    print(alist)
def jiujiu():
    for i in range(1,10):
        a=i+1
        for j in range (1,a):
            print('%s*%s=%s'%(j,i,j*i),end=' ')
        print('')
def paixu():
    blist=[9,8,4,2,1,3,7,5,10,6]
    for i in range(len(blist)-1):
        for j in range(len(blist)-1-i):
            if blist[j]<=blist[j+1]:
                continue
            temp=blist[j]
            blist[j]=blist[j+1]
            blist[j+1]=temp
    print(blist)


if __name__ == '__main__':
    maopao()
    jiujiu()
    paixu()