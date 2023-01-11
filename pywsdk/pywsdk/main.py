import cowsay

from toolbox.module_a import do_a_thing as test_a
from toolbox.module_b import do_a_thing as test_b


def main() -> None:
    test_a()
    test_b()

    cowsay.dragon("I am PYWSDK")
