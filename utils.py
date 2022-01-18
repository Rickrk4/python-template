import sys

def get_arguments():
    i = 1
    args = {}
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg[:2] == '--':
            vett = arg[2:].split('=', 1)
            key = vett[0]
            value = vett[1] if len(vett) > 1 else True
            args[key] = value
            i += 1
        else:
            break
    return args, sys.argv[i:]