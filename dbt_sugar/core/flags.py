"""Flags module containing the FlagParser "Factory"."""
import sys
from argparse import ArgumentParser
from typing import List


class FlagParser:
    """Sets flags from defaults or by parsing CLI arguments.

    In order to not have to always parse args when testing etc. We set the defaults explicitly here.
    This is a bit strict and not very DRY but it saves from surprises which for now is good.
    """

    def __init__(self, cli_parser: ArgumentParser) -> None:
        """Constructor for FlagParser.

        Holds explicit defaults and consumes parsed flags if asked for it.

        Args:
            cli_parser (ArgumentParser): CLI parser.
        """
        self.cli_parser = cli_parser
        self.model: str = "test_model"
        self.log_level: str = "debug"
        self.traceback_stack_depth: int = 4

    def consume_cli_arguments(self, test_cli_args: List[str] = list()) -> None:
        if test_cli_args:
            _cli_args = test_cli_args
        else:
            _cli_args = sys.argv[1:]
        self.args = self.cli_parser.parse_args(_cli_args)

        self.task = self.args.command

        # base flags that need to be set no matter what
        if self.args:
            self.log_level = self.args.log_level
            self.full_tracebacks = self.args.full_tracebacks

        # task specific args consumption
        if self.task == "doc":
            self.model = self.args.model