from argparse import ArgumentParser

parser: ArgumentParser = ArgumentParser(description="Try Hacke Me Controller")

parser.add_argument(
    "--cpu",
    "-c",
    help="Total parallel CPU",
    type=int,
    default=4,
)

services = parser.add_mutually_exclusive_group()

services.add_argument(
    "--subdomain",
    "-s",
    action="store_true",
)

services.add_argument(
    "--stop-subdomain",
    "-ss",
    action="store_true",
)

services.add_argument(
    "--port",
    "-p",
    action="store_true",
)

services.add_argument(
    "--stop-portscan",
    "-sp",
    action="store_true",
)
