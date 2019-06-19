import logging


logger = logging.getLogger(__name__)


def create_link(host, issue, summary):
    issue_link = f'{host}/browse/{issue}'
    sequence = f'\033]8;id={issue};{issue_link}\a{issue}: {summary}\a\033]8;;\a'

    return sequence
