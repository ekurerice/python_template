# coding: utf-8
# Date:
# Filename:

import os
import sys
import argparse
from logging import Formatter, getLogger, StreamHandler, DEBUG, WARNING, FileHandler

__author__ = ""
__date__ = ""

""" variables """
formatter = Formatter('%(asctime)-15s - %(levelname)-8s - %(message)s')
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# handler1
handler = StreamHandler(sys.stdout)
handler.setFormatter(formatter)

# handler2 (file)
# handler2 = FileHandler("test.log")
# handler2.setLevel(WARNING)
# handler2.setFormatter(formatter)

logger.addHandler(handler)
# logger.addHandler(handler2)


def main(options={}):
    """ 関数の説明タイトル

    関数についての説明文

    Args:
        引数の名前 (引数の型): 引数の説明

    Returns:
        戻り値の型: 戻り値の説明 (例 : True なら成功、False なら失敗)
    """
    
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
