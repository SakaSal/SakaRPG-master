import argparse
import races
# import goblin

game = open("myGame.txt", "w")

parser = argparse.ArgumentParser(description='SakaRPG')
parser.add_argument('-c', '--create', type=str, metavar='',
                    help="create a new character")
args = parser.parse_args()


if args.create:
    new = races.Human(args.create)
    game.write(f'{args.create} \n')
    game.write(f'{new.atribs}')

game = open("myGame.txt")
content = game.read()


game.close()
print(content)
