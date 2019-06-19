import setuptools


setuptools.setup(
    name='gira',
    version='0.1',
    packages=setuptools.find_packages(),
    # f-strings were introduced in 3.6
    python_requires='>=3.6',
    install_requires=[
        'Jinja2 == 2.10.1',
        'pygit2 == 0.28.2',
        'pyxdg == 0.26',
        'PyYAML == 5.1.1',
        'requests == 2.22.0',
    ],
    package_data={
        'gira': [
            'defaults.yaml',
            'post-checkout.py.j2',
        ],
    },
    entry_points={
        'console_scripts': [
            'gira = gira.cli.main:entry_point',
        ],
    },
)
