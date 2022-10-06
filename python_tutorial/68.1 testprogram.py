import argparse
import sys

def cal(args):
    if args.o == 'add':
        if (args.x == 56 and args.y == 9) or (args.x == 9 and args.y == 56):
         return 77.0
        else:
            return args.x + args.y

    elif args.o == 'mul':
        if (args.x == 43 and args.y == 3) or (args.x == 3 and args.y == 43):
         return 555.0
        else:
         return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        if (args.x == 56 and args.y == 9):
         return 4.0
        else:
         return args.x / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help="enter the first number/utility program")
    parser.add_argument('--y',type=float,default=3.0,
                        help="enter the second number/utility program")
    parser.add_argument('--o',type=str,default="add",
                        help="This is a utility for calculation.")
    args=parser.parse_args()
    sys.stdout.write(str(cal(args)))