"""This CLI tool uses argparse to do command-line execution without GUI of the analysis tools we build.

"""
import argparse # for building the CLI parsers
from cli.commands import fetch, correlate

def build_parser():
    # The centralized parser delegates subparsers to each command, that will each run a run(args).
    parser = argparse.ArgumentParser(prog="ticker-core", description="Visualizes market correlations.")
    subparsers = parser.add_subparsers(dest="commands")

    # We add an argument --correlation to apply Pearson Correlation to price movements.
    correlation_parser = subparsers.add_parser("correlate")
    correlation_parser.add_argument("-t", "--tickers", nargs="+", required=True)
    correlation_parser.add_argument("-p", "--period", nargs="+", required=True)
    correlation_parser.add_argument("-i", "--interval", nargs="+", required=True)
    correlation_parser.set_defaults(func=correlate.run)

    # We add an argument --tickers to indicate we want the user to use the argument to process ticker data.
    fetch_parser = subparsers.add_parser("fetch")
    fetch_parser.add_argument("-t", "--tickers", nargs="+", required=True)
    fetch_parser.set_defaults(func=fetch.run) # We set the call function to run(args) in fetch.py.
    fetch_parser.add_argument("-i", "--interval", nargs="+", required=True)
    fetch_parser.add_argument("-p", "--period", nargs="+", required=True)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()