n=0
score=0
l=['apple','banana','mango','green','pink']
def arr(word):
    global score
    if (word in l):
        print('correct')
        score=score+1
    else:
        score=score-1
        print('wrong')
for i in range(0,5):
    l2=['leppa','aannab','anogm','eerng','iknp']
    for e in range(n,i+1):
        print('Arrange the letters to form the valid word:',l2[e])
        word=input()
        n+=1
        arr(word)
print('Net score is',score)