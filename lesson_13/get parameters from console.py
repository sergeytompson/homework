import argparse
from ticket import make_ticket

parser = argparse.ArgumentParser('Create a ticket')

parser.add_argument('-fio', dest='fio', type=str, required=True)
parser.add_argument('-from', dest='from_', type=str, required=True)
parser.add_argument('-to', dest='to', type=str, required=True)
parser.add_argument('-date', dest='date', type=str, required=True)
parser.add_argument('-save_to', dest='save_to', type=str)

args = parser.parse_args()

make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save_to=args.save_to)
