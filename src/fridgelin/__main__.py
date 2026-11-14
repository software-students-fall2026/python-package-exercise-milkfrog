import argparse
import sys

from fridgelin import name, menu, review, drink





def main():


    parser=argparse.ArgumentParser( prog = "fridgelin",description="Turn whatever is in your fridge into a tasting menu.")

    parser.add_argument( "food", nargs = "+", help = "one to eight things from the fridge, quote the ones with spaces")
    parser.add_argument( "--level", type = int, default = 3, help = "how fancy, 1 to 5")
    parser.add_argument( "--courses", type = int, default =3, help="courses on the menu, 1 to 6")
    parser.add_argument("--width", type=int, default=72, help="menu width in columns, 40 to 120")
    parser.add_argument( "--stars",type=int,default=3,help= "stars for the review, 1 to 5")
    parser.add_argument( "--critic",default= "Percival Crumb",help= "who signs the review")
    parser.add_argument( "--budget",default="student",help= "student, date or investor")
    parser.add_argument("--seed",type=int,default = None,help="same seed, same output")
    parser.add_argument("--only",choices=["name","menu","review","drink","all"],default="all",help="print just one part")

    args = parser.parse_args()
    parts = []


    try:
        dish = name( args.food, args.level, args.seed)

        if args.only in ( "name", "all"):
            parts.append(dish)

        if args.only in ( "menu", "all"):
            parts.append(menu(args.food, args.level, args.courses, args.width, args.seed))

        if args.only in ( "review", "all"):
            parts.append(review(dish, args.stars, args.critic, args.seed))

        if args.only in ( "drink", "all"):
            parts.append(drink(dish, args.budget, args.seed))

    except (TypeError, ValueError) as err:
        print("fridgelin: " +str(err), file=sys.stderr)
        sys.exit(2)



    print("\n\n".join(parts))





if __name__=="__main__":
    main()


