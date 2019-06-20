import gira.config
import gira.git
import logging
import pygit2
import re
import sys


logger = logging.getLogger(__name__)


def setup_logging(level):
    loggers = logging.getLogger('gira')

    loggers.setLevel(level)

    logger_handler = logging.StreamHandler()
    loggers.addHandler(logger_handler)

    logger_formatter = logging.Formatter(
        'gira: %(levelname)s: %(message)s',
    )

    logger_handler.setFormatter(
        logger_formatter,
    )

    return


def entry_point():
    config = gira.config.load()

    setup_logging(
        level=config['logging']['hook'],
    )

    previous_head = sys.argv[1]
    new_head = sys.argv[2]

    logger.debug(
        'Previous HEAD: %s',
        previous_head,
    )

    logger.debug(
        'Current HEAD: %s',
        new_head,
    )

    flag = sys.argv[3]

    if flag == '1':
        logger.debug(
            'Branch checkout',
        )

        branch = gira.git.get_branch_name(new_head)

        logger.debug(
            'Name of checked-out branch: %s',
            branch,
        )

        gira.refresh.refresh(
            branch=branch,
        )
    else:
        logger.debug(
            'File checkout',
        )

    return
