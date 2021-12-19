def astrisk(star):
    for i in range(star,0,-1):
        print('*'*i)

if __name__=='__main__':
    star=int(input('Enter number of star: '))

    astrisk(star)
