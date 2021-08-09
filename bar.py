import foo
import helper_functions


def bar():
    return foo.foo() + "bar"


def baz():
    return helper_functions.foo() + "baz"


if __name__ == "__main__":
    print(bar())
    print(baz())

