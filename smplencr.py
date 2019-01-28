import os
os.chdir('E:\Docs\python')
import encry as en
c=int(input('1.Encrypt\t2.Decrypt\t Choice:  '))
f=input('Enter the data : ')
if c==1:
    print('The Encrypted data and the key are  :',end='')
    print(en.encr(f))
elif c==2:
    ke=input('Enter the key to decrypt : ')
    print('tHe dEcRyPtEd CoNtEnT iS ',en.decr(f,ke))
