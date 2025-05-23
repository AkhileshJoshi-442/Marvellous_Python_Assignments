def vowelcheck(val):
    if val=="a":
        print(val,"is a vowel")
    elif val=="e":
        print(val,"is a vowel")
    elif val=="i":
        print(val,"is a vowel")
    elif val=="o":
        print(val,"is a vowel")
    elif val=="u":
        print(val,"is a vowel")
    else:
        print(val,"is a consonant")

        

def main():
    print("enter a character")
    value=input()
    vowelcheck(value)

if __name__=="__main__":
    main()