def vowelcheck(val):
    vowel=["a","e","i","o","u"]
    if val in vowel:
        print(val,"is a vowel")
    else:
        print(val,"is a consonant")
        

def main():
    print("enter a character")
    value=input()
    vowelcheck(value)

if __name__=="__main__":
    main()