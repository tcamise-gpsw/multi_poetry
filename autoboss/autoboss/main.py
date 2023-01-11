import cowsay

from shared.toolbox.package_a.module_a import do_a_thing as test_a
from shared.toolbox.package_b.module_b import do_a_thing as test_b


def main() -> None:
    test_a()
    test_b()

    cowsay.dragon("I am autoboss")
