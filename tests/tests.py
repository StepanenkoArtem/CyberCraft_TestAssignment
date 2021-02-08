import json
from unittest.mock import patch

from django.test import Client

client = Client()

TARGET_URL = ''


def test_repo_list_login_not_exist():
    """Check responce if requested login does not exist on GitHub."""
    responce = client.get(TARGET_URL, {'github_login': 'no_existing_login'})
    assert not responce.context['github_owner']
    assert responce.context['error']


def test_repo_list_is_empty():
    """Check responce if requested login exists but have no repos."""
    mocked_responce = 'tests/fixtures/mocked_responces/owner_has_no_nodes.json'
    # mocking Github responce
    # repository owner exist and has no nodes
    with patch('repos.github.fetch_owner_data') as mocked:
        mocked.return_value = json.loads(open(mocked_responce).read())
        # make test GET request '?github_login=owner_has_no_nodes'
        responce = client.get(
            TARGET_URL,
            {'github_login': 'owner_has_no_nodes'},
        )
    # load expected data
    with open('tests/fixtures/expected/owner_has_no_nodes.json') as expected:
        expected_responce = json.loads(expected.read())
    assert responce.context['github_owner'] == expected_responce


def test_repo_list():
    """Check responce if requested login exists and have node(s)."""
    # mocking Github responce
    # repository owner exist and has nodes
    mocked_responce = 'tests/fixtures/mocked_responces/owner_has_nodes.json'
    with patch('repos.github.fetch_owner_data') as mocked:
        mocked.return_value = json.loads(open(mocked_responce).read())
        # make test GET request '?github_login=dhh'
        responce = client.get(TARGET_URL, {'github_login': 'dhh'})

    # load expected data
    with open('tests/fixtures/expected/owner_has_nodes.json') as expected:
        expected_responce = json.loads(expected.read())

    assert responce.context['github_owner'] == expected_responce
