import gira.config
import gira.jira
import gira.save
import gira.term
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


def get_branch_name(head_ref):
    repository = pygit2.Repository('.')

    #head = repository.lookup_reference(head_ref)
    head = repository.head

    name = head.shorthand

    return name


def branch_corresponds_to_ticket(branch, regex):
    match = re.match(
        regex,
        branch,
    )

    group = match.group(1).upper()
    number = match.group(2)

    issue = f'{group}-{number}'

    return issue


def entry_point():
    config = gira.config.load()

    setup_logging(
        level=config['logging'],
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

        branch = get_branch_name(new_head)

        logger.debug(
            'Name of checked-out branch: %s',
            branch,
        )

        try:
            issue = branch_corresponds_to_ticket(
                branch=branch,
                regex=config['git']['issue-regex'],
            )
        except:
            logger.debug(
                'Branch does not belong to any issue',
            )
        else:
            logger.debug(
                'Branch corresponds to issue %s',
                issue,
            )

            try:
                summary = gira.jira.get_issue_summary(
                    host=config['jira']['host'],
                    issue=issue,
                    login_password=config['jira']['auth']['password'],
                    login_user=config['jira']['auth']['username'],
                )
            except:
                logger.error(
                    'Cannot get summary of issue %s',
                    issue,
                )
                pass
            else:
                sequence = gira.term.create_link(
                    host=config['jira']['host'],
                    issue=issue,
                    summary=summary,
                )

                gira.save.save(
                    branch=branch,
                    sequence=sequence,
                )
    else:
        logger.debug(
            'File checkout',
        )

    return
