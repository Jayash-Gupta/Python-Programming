play1=input()
play2=input()
dec1=input()
dec2=input()
a='Rock'
b='Paper'
c='Scissor'
if (dec1==a and dec2==b):
    print(play2, end=' ')
    print('Win')
    
elif (dec1==a and dec2==c):
    print(play1, end=' ')
    print('Win')
    
elif (dec1==b and dec2==a):
    print(play1, end=' ')
    print('Win')
    
elif (dec1==b and dec2==c):
    print(play2, end=' ')
    print('Win')
    
elif (dec1==c and dec2==a):
    print(play2, end=' ')
    print('Win')
    
else:
    print(play1, end=' ')
    print('Win')
