'''This Module contains Algorithm for Encryption and Decryption
                   written by

*    *        ****** ****** *    *              *
*    *   **   *    * *    * *    *   **        *
*    *  *  *  *    * *      *    *  *  *      *
****** ****** *****  *****  ****** ******    *****************************
*    * *    * *    *      * *    * *    *     *
*    * *    * *    * *    * *    * *    *      *
*    * *    * *    * ****** *    * *    *       *

                   '''
import random
import string
def keygen():
    '''keygen()  -  generate random keys'''
    b=random.randint(10,99)
    a=random.randint(10,50)
    return a,b
def dic(ke,a,en=True):
    '''dic(list,int,bool)  -  create a dictionary'''
    d=list(string.printable)
    e=list(int(str(i**a)[:6:]) for i in [j for j in range(32,127)])
    s={}
    if en==True:
        s=dict(zip(e,d))
    else:
        s=dict(zip(d,e))
    try:
        k=[s[i] for i in ke]
        return k
    except Exception as EX:
        k=[]
        for i in range(len(ke)):
            k.append(random.choice(string.printable))
        return k
def encr(q):
    '''encr(string)  -  encrypt the data'''
    a,b=keygen()
    f=list(q)
    f.reverse()
    j=dic(f,a,en=False)
    g=[str(i^b) for i in j]
    y=[]
    for i in g:
        while len(i)<6:
            i+=random.choice(string.punctuation)
        y.append(i)
    s=''.join(y)
    try:
        z=[int(s[i-2:i:]) for i in range(2,len(s)+1,2)]
        q=''
        for i in z:
            if i <60:
                i+=200
            if i==92:
                i+=907
            q+=chr(i)
        return q,str(a)+':'+str(b)
    except Exception as EX:
        return s,str(a)+':'+str(b)
def decr(p,q):
    '''decr(string,string)  -  decrypt the data;key-based'''
    try:
        a,b=(int(i) for i in q.split(':'))
    except ValueError as VE:
        a,b=(random.randint(10,99) for i in range(2))
    if any(c.isdigit() for c in p):
        s=p
    else:
        w=[ord(i) for i in p]
        s=''
        for i in w:
            if i==999:
                i-=907
            if i>=200:
                i-=200
            if i<10:
                s+='0'
            s+=str(i)
    d=[s[i-6:i:] for i in range(6,len(s)+1,6)]
    try:
        h=[]
        for i in d:
            for j in string.printable[10::]:
                if j in i:
                    i=i[:i.index(j):]+i[i.index(j)+1::]
            h.append(i)
    except Exception as IE:
        h=[]
        for i in range(len(s)//6):
            h.append(str(random.randint(100000,1000000)))
    g=[((~(int(i)^b)+1)*-1) for i in h]
    s=dic(g,a)
    s.reverse()
    f=''.join(s)
    return f
