"""Xtrabackup for Monsoon
"""

from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="monsoon-backup-xtrabackup",
    version="0.1.1",
    description="Monsoon plug-in for Percona XtraBackup backups.",
    long_description=LONG_DESCRIPTION,
    url="https://github.ibm.com/apset/monsoon-backup-xtrabackup",
    author="Luiz Aoqui",
    author_email="laoqui@ca.ibm.com",
    license="IBM",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Database",
        "Topic :: System :: Archiving :: Backup",
        "Topic :: Utilities"
    ],
    packages=find_packages(),
    install_requires=[
        "monsoon-cli>=0.1.4"
    ],
    entry_points={
        "monsoon.backups": [
            "xtrabackup=xtrabackup:XtraBackupBackup"
        ]
    }
)
