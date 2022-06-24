import pytest

# def add(x,y):
#     return x+y

# def test1():
#     assert 2 == add(1,1)
#
# def test2():
#     assert 1 != add(1,1)
#
# def test3():
#     assert 3 == add(1,1)

# ！！！传递一组参数进行测试，很重要！！！
# @pytest.mark.parametrize(
#     "x,y,expected",
#     [
#         (1,1,2),
#         (2,3,5),
#         (5,8,13),
#     ]
# )

# def test_add(x,y,expected):
#     assert add(x,y) == expected
# def func(x):
#     if x==0:
#         raise ValueError("value error!")
#     else:
#         pass
#
#
# def test_func1():
#     with pytest.raises(ValueError):
#         func(0)
#
#
# def test_func2():
#     assert func(1) == None

# ！！！分组测试的概念，很重要！！！

@pytest.mark.g1
def test_func1():
    pass


@pytest.mark.g2
def test_func2():
    pass


@pytest.mark.g1
def test_func3():
    pass


@pytest.mark.g2
def test_func4():
    pass


@pytest.mark.g1
def test_func5():
    pass