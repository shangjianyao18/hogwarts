def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用户名和用例标识nodeid的中文显示出
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf_8").decode("unicode_escape")
