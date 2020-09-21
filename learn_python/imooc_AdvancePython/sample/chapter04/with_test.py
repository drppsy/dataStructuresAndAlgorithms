# try except finally
'''
1. finally一般用来做资源的释放
2. finally有return的话，有限return finally，再从其他语句中return
'''


def try_test():
    try:
        print("try")
        raise KeyError
        return 1
    except KeyError as e:
        print("KeyError")
        return 2
    else:
        print("other error")
        return 3
    finally:
        return 4


'''
上下文管理器，enter、exit魔法函数
'''
class Sample:

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def do_somethin(self):
        print("do_something")

with Sample() as sample:
    sample.do_somethin()

# if __name__ == "__main__":
#     t = try_test()
#     print(t)