from base import parser
from argparse import Namespace


class Cli:

    def __init__(self, params: Namespace):
        self.params: Namespace = params

    def start(self):
        breakpoint()


if __name__ == "__main__":
    ar = parser.parse_args()
    Cli(params=ar).start()
