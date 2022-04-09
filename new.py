import random



def main():
    name=input("Enter your name:- ")
    msg=["good","bad","awful","cheap","bummer","abominable","poopy","raunchy","stinking","unsatisfactory","cheesy","incorrect","grungy","crappy","wonderful","spanking","boss","positive","worthy","admirable","neat","deluxe","splendid","tiptop","precious","pleasing"]
    ans=random.choices(msg)
    print(f"Hay! {name} you are, {ans}")
    
    rep=input("Do you want to play again? Enter y/n:- ").lower()
    if rep=="y":
        main()
    elif rep=="n":
        input("Press [Enter] to quit.")
        exit()
    else:
        input("Press [Enter] to quit. Dumb person can you not press 'n'? ")
        exit()
main()        




