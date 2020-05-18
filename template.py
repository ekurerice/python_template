# coding: utf-8
# Date:
# Filename:

import os
import sys
import argparse
from logging import Formatter, getLogger, StreamHandler, DEBUG, WARNING

__author__ = 'rindybell'
__date__ = ""

""" variables """
formatter = Formatter('%(asctime)-15s - %(levelname)-8s - %(message)s')
logger = getLogger(__name__)
handler = StreamHandler(sys.stdout)
handler.setLevel(WARNING)
handler.setFormatter(formatter)
logger.addHandler(handler)


def main(options={}):
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__file__)

    # parser.add_argument("--config", type=str,
    #                     help=u"config",
    #                     required=True)

    args = parser.parse_args()
    options = args.__dict__

    main(options)
