import random
colours=['Black','Red','Blue','Pink']
shape=['Spade','Club','Heart','Diamond']
num=[1,2,3,4]
r_col=random.choice(colours)
r_sh=random.choice(shape)
r_ch=random.choice(num)
if r_col=='Black' and r_sh=='Spade' and r_ch==4:
    print("You Won Lucky Draw...You WON 2 Crs")
else:
    print("Better Luck Next Time")
    print("You got:{} {} {}".format(r_col,r_sh,r_ch))