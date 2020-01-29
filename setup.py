from setuptools import setup, find_packages


with open("version.txt", "r") as fh:
    pkg_version = fh.read()

setup(
    name='app',
    version=pkg_version,
    author="Giragadurai Vallirajan",
    author_email="gvallirajan@relevancelab.com",
    description="Dark Launch Demo",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)