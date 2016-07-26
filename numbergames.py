import random 
number=35
for i in range(25):
     a = random.randint(30,40);
     if number==a:
        print ' YOU WIN!!!!(:'
        break
     else:
         if a > number:
             print 'lower'
         else:
             print 'higher'  
         print 'YOU LOSE'
         
