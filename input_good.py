def cc_good(x, y):
    r = x
    if x > 5:
        r = 5
    if y < 5:
        r = y
    return r


class Foo:
    i = 1

    def foo(self):
        pass

    class Bar:
        ii = 2

        def bar(self):
            pass

        class Baz:
            iii = 3

            def baz(self):
                pass
