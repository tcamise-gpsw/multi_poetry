import cowsay

from toolbox.package_a.main import do_a_thing as test_a
from toolbox.package_b.main import do_a_thing as test_b


def main() -> None:
    test_a()
    test_b()

    cowsay.dragon("I am PYWSDK")
