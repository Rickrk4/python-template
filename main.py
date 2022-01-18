from utils import get_arguments

def main(target, args={}):
    pass

if __name__ == "__main__":
    args, targets = get_arguments()
    for target in targets:
        main(target, args)