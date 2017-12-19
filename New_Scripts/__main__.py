from argparse import ArgumentParser

argu = ArgumentParser(prog="New_Scripts")
argu.add_argument("id", type=int)

parse_arg = argu.parse_args()

print(parse_arg)