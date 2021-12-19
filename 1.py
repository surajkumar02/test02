def even_char(text):
    for i in range(1,len(text),2):
        print(text[i])

if __name__=='__main__':
    text=(input('Enter text: '))

    even_char(text)