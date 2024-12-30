import calculator


def test_first():
    a = 1
    b = 1
    assert a + b == calculator.Calculator().add(1, 1)
