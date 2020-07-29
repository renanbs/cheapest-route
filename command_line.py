import sys

from api.cmd.routes import process

if __name__ == '__main__':
    response = process(sys.argv)
    if response == -1:
        exit(response)
