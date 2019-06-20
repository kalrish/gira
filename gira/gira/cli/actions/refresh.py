import gira.git
import gira.jira
import gira.refresh
import gira.term
import logging
import os


logger = logging.getLogger(__name__)


def setup(subparsers, config):
    parser_get = subparsers.add_parser(
        'refresh',
        help='refresh cached Jira issue summaries',
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

    return


def branch_corresponds_to_ticket(branch, regex):
    match = re.match(
        regex,
        branch,
    )

    group = match.group(1).upper()
    number = match.group(2)

    issue = f'{group}-{number}'

    return issue


def action(args):
    branch = gira.git.get_branch_name(new_head)

    gira.refresh.refresh(
        branch=branch,
    )

    return 0
