import argparse
import sys

def cal(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
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

    """
    1.open command prompt 
    2.reach to the file destination
    3. filename arguments 
      or 
      python filename.extension arguments
    """