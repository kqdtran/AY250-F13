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
