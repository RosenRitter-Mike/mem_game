import random as rnd
from art import *

idx_list: list[str] = [str(i) for i in range(12)];
deck: list[str] = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"];
rnd.shuffle(deck);

def print_list(l1: list[str])->None:
    print("", l1[0:4], "\n", l1[4:8], "\n", l1[8:12], "\n")
    return;


def flip_card(list_a: list[str], list_b: list[str], idx: int) -> None:
    list_b[idx] = list_a[idx];
    print_list(list_b);
    return;


def check_choice(choi: str) -> int:
    if choi.upper() == "R":
        return 99;
    elif int(choi) > 11 or int(choi) < 0:
        print(f"invalid choice for card1, choose again.");
        return 98;
    else:
        return int(choi);


def card_game(my_deck: list[str]) -> None:
    cards: list[str] = ["_" for _ in my_deck]
    rnd.shuffle(my_deck);
    while True:
        print_list(idx_list);
        print_list(cards);
        choi1: str = input("Input the index of the first chosen card: ");
        try:
            c1: int = check_choice(choi1);
            if c1 == 99:
                tprint("game   restarted", "chunky");
                card_game(my_deck);
                return None;
            elif c1 == 98 or cards[c1] != "_":
                print(f"{choi1} is an invalid choice for first card, choose again.");
                continue;
            else:
                flip_card(my_deck, cards, c1);
        except Exception as e:
           print("The error is: ", e);
        choi2: str = input("Input the index of the second chosen card: ");
        try:
            c2 = check_choice(choi2);
            if c2 == 99:
                tprint("game restarted", "chunky");
                card_game(my_deck);
                return None;
            elif c2 == 98 or cards[c2] != "_":
                print(f"{choi2} is an invalid choice for the second card, choose again.");
                continue;
            else:
                flip_card(my_deck, cards, c2);

            print(f"first card: {my_deck[c1]}, second card: {my_deck[c2]}");
            if my_deck[c1] == my_deck[c2]:
                cards[c1] = my_deck[c1];
                cards[c2] = my_deck[c2];
                tprint("It's a match!", "chunky");
                print(art("cheers")*4,"\n\n");
            else:
                cards[c1] = "_";
                cards[c2] = "_";
                tprint("guess again!", "chunky");
                print(art("dunno2")*8, "\n\n");
        except Exception as e:
            print("The error is: ", e);
       
        if "_" not in cards:
            tprint("You\nhave\n won!!\nCongratulations!!", "epic");
            print(art("dance"));
            if input("do you want to play another game? (y/n) ").upper() == "Y":
                card_game(my_deck);
                return None;
            else:
                return None;


card_game(deck);

