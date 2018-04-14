#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    author="chenjiandongx",
    author_email="chenjiandongx@qq.com",
    name="gh-contributors",
    version="0.1.0",
    license="MIT",
    url = "https://github.com/chenjiandongx/gh-contributors",
    py_modules=["gh_contributors"],
    description="Generate contributors.md via the command line",
    entry_points={
        'console_scripts': ['gh-c=gh_contributors:command_line_runner']
    }
)
