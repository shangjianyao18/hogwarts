def pytest_collection_modifyitems(items):
    # 用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")