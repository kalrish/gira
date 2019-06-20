import argparse
import gira.config
import gira.cli.actions.get
import gira.cli.actions.install
import gira.cli.actions.refresh
import logging


logger = logging.getLogger(__name__)


def setup_argparser(config):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--debug',
        help='enable debugging',
        required=False,
        action='store_true',
        dest='debug',
    )

    parser.add_argument(
        '-l, --log',
        help='log level',
        required=False,
        choices=[
            'debug',
            'info',
            'warning',
            'error',
        ],
        #default=config['logging']['cli'],
        default='info',
        dest='log_level',
    )

    subparsers = parser.add_subparsers(
        help='actions',
        dest='action',
    )

    gira.cli.actions.get.setup(
        subparsers,
        config,
    )
    gira.cli.actions.install.setup(
        subparsers,
        config,
    )
    gira.cli.actions.refresh.setup(
        subparsers,
        config,
    )

    return parser


def setup_logging(level):
    logging_level = getattr(
        logging,
        level.upper(),
    )

    logging.basicConfig(
        format='%(name)s: %(levelname)s: %(message)s',
        level=logging_level,
    )

    return


actions = {
    'get': gira.cli.actions.get.action,
    'install': gira.cli.actions.install.action,
    'refresh': gira.cli.actions.refresh.action,
}


def entry_point():
    config = gira.config.load()

    parser = setup_argparser(config)

    args = parser.parse_args()

    setup_logging(
        level=args.log_level,
    )

    action = actions[args.action]

    if args.debug:
        exit_code = action(args)
    else:
        try:
            action(args)
        except:
            exit_code = 1
            pass
        else:
            exit_code = 0

    return exit_code
