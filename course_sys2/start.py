import sys
import os

from core import src
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

if __name__ == '__main__':
    src.run()
