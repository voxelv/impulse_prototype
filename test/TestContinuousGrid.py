from unittest import TestCase
from impulse_lib.ContinuousGrid import ContinuousGrid


class TestContinuousGrid(TestCase):
    def test_default_param(self):
        g = ContinuousGrid(default="*")
        g.set(0, 0, "-")
        g.set(1, 1, "-")
        actual = g.__str__()
        expect = "*-\n-*\n"
        self.assertEqual(actual, expect, "FAILED: grid string \n{}\ndoes not match\n{}".format(actual, expect))

    def test_set(self):
        g = ContinuousGrid("_")
        g.set(1, 1, "X")
        self.assertEqual(g.__str__(), "X\n", "WOW SUCH PASS MSG")
        g.set(0, 0, "Y")
        actual = g.__str__()
        expect = "_X\nY_\n"
        self.assertEqual(actual, expect, "FAILED: grid string \n{}\ndoes not match\n{}".format(actual, expect))
        g.set(4, 4, "Z")
        actual = g.__str__()
        expect = "____Z\n_____\n_____\n_X___\nY____\n"
        self.assertEqual(actual, expect, "FAILED: grid string \n{}\ndoes not match\n{}".format(actual, expect))
        g.set(-1, -1, "A")
        actual = g.__str__()
        expect = "_____Z\n______\n______\n__X___\n_Y____\nA_____\n"
        self.assertEqual(actual, expect, "FAILED: grid string \n{}\ndoes not match\n{}".format(actual, expect))
        g.set(-1, 2, "B")
        actual = g.__str__()
        expect = "_____Z\n______\nB_____\n__X___\n_Y____\nA_____\n"
        self.assertEqual(actual, expect, "FAILED: grid string \n{}\ndoes not match\n{}".format(actual, expect))
        g.set(2, -1, "C")
        actual = g.__str__()
        expect = "_____Z\n______\nB_____\n__X___\n_Y____\nA__C__\n"
        self.assertEqual(actual, expect, "FAILED: grid string \n{}\ndoes not match\n{}".format(actual, expect))

    def test_get(self):
        g = ContinuousGrid("_")
        g.set(0, 0, "X")
        actual = g.get(0, 0)
        expect = "X"
        self.assertEqual(actual, expect, "FAILED: get returned {}, expected {}".format(actual, expect))
        actual = g.get(1, 1)
        expect = "_"
        self.assertEqual(actual, expect, "FAILED: get returned {}, expected {}".format(actual, expect))

    def test_pop(self):
        g = ContinuousGrid("_")
        g.set(0, 0, "X")
        actual = g.pop(0, 0)
        expect = "X"
        self.assertEqual(actual, expect, "FAILED: get returned {}, expected {}".format(actual, expect))
        actual = g.pop(0, 0)
        expect = "_"
        self.assertEqual(actual, expect, "FAILED: get returned {}, expected {}".format(actual, expect))
