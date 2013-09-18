"""Testing code for CalCalc.py.
Add your own tests below, and make sure to follow the
format. Instructions on how to run the tests can be found
on the README.md file"""

from CalCalc import calculate


def test_1():
    assert calculate('2*2') - 4 < 0.0001


def test_2():
    assert calculate('4**3+7*8') == 120


def test_3():
    assert calculate('mass of the sun in kg').startswith('1.988435')


def test_4():
    assert calculate('im too awesome').startswith('Too bad')


def test_5():
    assert calculate('berkeley california').count('population') == 3
