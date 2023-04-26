import pytest

# 第一条，单参数情况
list1 = ['appium', 'selenium', 'pytest']


@pytest.mark.parametrize('name', ['appium', 'selenium', 'pytest'])
def test_param(name):
    assert name in list1


# 第二条，多参数情况
# ids，为用例添加别名，增加可读性，第二个参数中有几个值，ids就需要有几个值
@pytest.mark.parametrize("username, password", [['name1', 'password1'],
                                                ['name2', 'password2'],
                                                ], ids=['正确用户名密码', '错误用户名密码']
                         )
def test_login(username, password):
    print(f"输入的用户名为：{username},输入的密码为：{password}")


@pytest.mark.parametrize("test_input, exceptd", [("3+2", 5), ("5+9", 10)
                                                 ],
                         ids=["3+2的值等于5吗", "5+9的值等于10吗"]
                         )
def test_mark_more(test_input, exceptd):
    assert eval(test_input) == exceptd
