import logging
from xdg import BaseDirectory


logger = logging.getLogger(__name__)


def save(branch, sequence):
    cache_dir = BaseDirectory.save_cache_path('gira')

    path = f'{cache_dir}/{branch}'

    with open(path, 'w') as f:
        f.write(
            sequence,
        )

    return
