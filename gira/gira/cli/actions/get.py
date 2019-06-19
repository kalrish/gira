import gira.jira
import gira.term
import logging


logger = logging.getLogger(__name__)


def setup(subparsers, config):
    parser_get = subparsers.add_parser(
        'get',
        help='get Jira issue',
    )

    parser_get.add_argument(
        '--jira-host',
        help='Jira URL',
        required=not bool(config['jira']['host']),
        default=config['jira']['host'],
        dest='jira_host',
    )

    parser_get.add_argument(
        '--jira-auth',
        help='login data for Jira',
        nargs=2,
        metavar=(
            'username',
            'password',
        ),
        default=(
            config['jira']['auth']['username'],
            config['jira']['auth']['password'],
        ),
        dest='jira_auth',
    )

    parser_get.add_argument(
        'ticket',
        help='Jira issue',
    )

    return


def action(args):
    issue = args.ticket

    summary = gira.jira.get_issue_summary(
        host=args.jira_host,
        issue=issue,
        login_password=args.jira_auth[1],
        login_user=args.jira_auth[0],
    )

    logger.info(
        'Summary of issue %s: %s',
        issue,
        summary,
    )

    sequence = gira.term.create_link(
        host=args.jira_host,
        issue=args.ticket,
        summary=summary,
    )

    print(sequence)

    return 0
