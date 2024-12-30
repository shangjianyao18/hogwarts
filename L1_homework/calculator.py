class Calculator:
    def add(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入【-99~99】之间的数字")
            return "参数大小超出范围"

        return a + b

    def div(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99到99】之间的数字")
            return "参数大小超出范围"

        return a / b

def test_first():
    a = 1
    b = 1
    assert a + b == Calculator.add(a, b)
