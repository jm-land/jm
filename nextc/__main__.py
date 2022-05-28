import sys
from . import __version__

def main():
    sys.stderr.write(f'nextc: {__version__}')

if __name__ == '__main__':
    main()