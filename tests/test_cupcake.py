import sys
from os.path import abspath, dirname, join
sys.path.append(abspath(join(dirname(__file__), '..')))


from cupcake import __version__


def test_version():
    assert __version__ == '0.15.0'
