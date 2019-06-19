import logging
import requests
import requests.auth


logger = logging.getLogger(__name__)


def get_issue_summary(host, issue, login_user, login_password):
    response = requests.get(
        f'{host}/rest/api/latest/issue/{issue}',
        auth=requests.auth.HTTPBasicAuth(
            login_user,
            login_password,
        ),
    )

    summary = None

    if response.status_code == requests.codes.ok:
        response_data = response.json()

        summary = response_data['fields']['summary']

    if not summary:
        raise Exception

    return summary
