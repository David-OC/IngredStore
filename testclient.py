import sys
from ingredstore import IngredStore

def main(argv):
    ingredinst = IngredStore(argv[1])
    ingredients = ingredinst.get_ingredients()

    for item in ingredients:
        print item


if __name__ == "__main__":
    main(sys.argv)

