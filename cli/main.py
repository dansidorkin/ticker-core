"""This CLI tool uses argparse to do command-line execution without GUI of the analysis tools we build.

"""
import argparse

from cli.commands import fetch

def build_parser():
    # The centralized parser delegates subparsers to each command, that will each run a run(args).
    parser = argparse.ArgumentParser(prog="Markets", description="Visualizes market movements.")
    subparsers = parser.add_subparsers(dest="commands")
    fetch_parser = subparsers.add_parser("fetch")

    # We add an argument --tickers to indicate we want the user to use the argument to process ticker data.
    fetch_parser.add_argument("--tickers", nargs="+", required=True)

    # We set the call function to run(args) in fetch.py.
    fetch_parser.set_defaults(func=fetch.run)

    return parser



def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()