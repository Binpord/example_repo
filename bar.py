from foo import foo


def bar():
    return foo() + "bar"


if __name__ == "__main__":
    print(bar())

