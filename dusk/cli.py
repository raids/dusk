# -*- coding: utf-8 -*-

import argparse
import logging
import sys

from . import __version__
import profiler


def parse_arguments(args):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--debug", action="store_true",
        default=False, help="enable debug logs"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version="ptolemy version {0}".format(__version__)
    )
    parser.add_argument(
        "-n", "--document-name", help="name of the ssm document to run"
    )
    parser.add_argument("instance_id", help="id of the instance to terminate")

    return parser.parse_args(args)


def setup_logger(debug):
    """
    Setup logging.
    :param debug: A boolean specifying whether the debug level should be set \
    to debug or critical
    :type debug: bool
    :returns: logging.Logger()
    """
    level = logging.DEBUG if debug else logging.CRITICAL
    logging.basicConfig(
        format="[%(asctime)s] - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=level
    )
    return logging.getLogger(__name__)


def cli():
    arguments = parse_arguments(sys.argv[1:])
    setup_logger(arguments.debug)
    main(arguments.instance_id)


def main(instance_id):
    profiler.run(instance_id)
