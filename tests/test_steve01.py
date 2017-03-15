#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_steve01
----------------------------------

Tests for `steve01` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from steve01 import steve01
from steve01 import cli


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')
    assert True


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    assert True


def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main, input="496")
    assert result.exit_code == 0
    assert 'Enter Number' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


@pytest.mark.parametrize("input,output", [
    (496, [1, 2, 4, 8, 16, 31, 62, 124, 248]),
    (3, [1]),
    (6, [1, 2, 3]),
    (5, [1])
])
def test_can_find_factors(input, output):
    l = steve01.findFactors(input)
    assert l == output


@pytest.mark.parametrize("input,output", [
    (6, True),
    (3, False),
    (496, True),
    (495, False),
    (17, False),
    (4, False)
])
def test_is_perfect_number(input, output):
    assert steve01.isPerfectNumber(input) == output


@pytest.mark.parametrize("input,factorlist", [
    ('496', '[1, 2, 4, 8, 16, 31, 62, 124, 248]'),
    ('6', '[1, 2, 3]'),
    ('5', '[1]')
])
def test_output_includes_factor_list(input, factorlist):
    runner = CliRunner()
    result = runner.invoke(cli.main, input=input)
    assert factorlist in result.output
