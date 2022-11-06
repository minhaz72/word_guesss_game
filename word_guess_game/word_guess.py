# let's play  a word game : 
a = str(input('enterb your word guess : '))
word= 'app',a,"e"
print(" let's guess the  hide character in  app_e ")
point= 0 
for i in range(5): 
    if a== 'l' or a== 'L': 
        point+=1 
        print("point",  point)
        print('win')
        break 
    else: 
        print( ' lose : ')
        point-=1 
        print('point', point)
        break 