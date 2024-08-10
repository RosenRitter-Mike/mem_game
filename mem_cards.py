import random as rnd


deck: list[str] = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"];
rnd.shuffle(deck);
# print(len(deck));
print("",deck[0:4],"\n",deck[4:8],"\n",deck[8:12],"\n")


def card_game(my_deck: list[str]) -> None:
    cards: list[str] = ["_" for _ in my_deck]
    rnd.shuffle(my_deck);
    while True:
        print("",cards[0:4],"\n",cards[4:8],"\n",cards[8:12],"\n")
        choi1: str = input("Input the index of the first chosen card: ");
        choi2: str = input("Input the index of the second chosen card: ");
        if choi1.upper() == "R" or choi2.upper() == "R":
            print("game restarted");
            card_game(my_deck);
            return None;
        elif int(choi1) > 11 or int(choi1) < 0:
            print("invalid choice, chose again.");
            continue;
        elif int(choi2) > 11 or int(choi2) < 0:
            print("invalid choice, chose again.");
            continue;
        else:
            c1 = int(choi1);
            c2 = int(choi2);
            if cards[c1] != "_" or cards[c2] != "_":
                print("invalid choice, choose again.");
                continue;
            print(f"first card: {my_deck[c1]}, second card: {my_deck[c2]}");
            if my_deck[c1] == my_deck[c2]:
                cards[c1] = my_deck[c1];
                cards[c2] = my_deck[c2];
                print("It's a match!");
            else:
                print("guess again!");


        if "_" not in cards:
            print("You have won!! Congratulations!!");
            if input("do you want to play another game? (y/n) ").upper() == "Y":
                card_game(my_deck);
                return None;
            else:
                return None;



card_game(deck);

