import setuptools

from pathlib import Path

p = Path('.').resolve()

setup_requires = [
]

install_requires = [
    'requests'
]
test_require = [
]

setuptools.setup(
    name="pybiodata",
    version='0.0.1',
    python_requires='>3.5',
    author="Koji Ono",
    author_email="kbu94982@gmail.com",
    description="library supporting for downloading bio-data.",
    url='https://github.com/0h-n0/pybiodata',
    long_description=(p / 'README.md').open(encoding='utf-8').read(),
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=test_require,
    extras_require={
        'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']},
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    entry_points = {
        'console_scripts' : ['pybiodata = pybiodata.entry_point:main'],
    },
)
