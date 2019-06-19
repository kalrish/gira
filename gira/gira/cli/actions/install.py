import jinja2
import logging
import os
import pygit2
import stat
import sys


logger = logging.getLogger(__name__)


def setup(subparsers, config):
    parser_install = subparsers.add_parser(
        'install',
        help='install git hooks',
    )

    parser_install.add_argument(
        '-f, --force',
        help='overwrite existing hooks',
        required=False,
        action='store_true',
        dest='force',
    )

    return


def render():
    jinja2_package_loader = jinja2.PackageLoader(
        package_name='gira',
        package_path='',
    )

    jinja2_environment = jinja2.Environment(
        loader=jinja2_package_loader,
        lstrip_blocks=True,
        trim_blocks=True,
    )

    template = jinja2_environment.get_template(
        'post-checkout.py.j2',
    )

    output = template.render(
        python=sys.executable,
    )

    return output


def action(args):
    path = '.'

    repository_path = pygit2.discover_repository(
        path,
    )

    repository = pygit2.Repository(repository_path)

    try:
        hooks_path = repository.config['core.hooksPath'].value
    except KeyError:
        hooks_path = f'{repository.path}/hooks'

    logger.debug(
        'git hooks directory: %s',
        hooks_path,
    )

    hook_path = f'{hooks_path}/post-checkout'

    script = render()

    open_mode = 'w' if args.force else 'x'

    try:
        f = open(
            hook_path,
            open_mode,
        )
    except FileExistsError:
        logger.warning(
            'Not overriding existing post-checkout hook',
        )
    else:
        f.write(script)

    st = os.stat(
        hook_path,
    )

    os.chmod(
        hook_path,
        st.st_mode | stat.S_IEXEC,
    )

    return 0
