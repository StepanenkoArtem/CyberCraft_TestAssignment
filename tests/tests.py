import json

from django.test import Client

client = Client()

TARGET_URL = ''


def test_repo_list_login_not_exist():
    """Check responce if requested login does not exist on GitHub."""
    responce = client.get(TARGET_URL, {'github_login': 'no_existing_login'})
    assert not responce.context['github_data']


def test_repo_list_login_is_empty():
    """Check responce if requested login exists but have no repos."""
    responce = client.get(TARGET_URL, {'github_login': 'empty_github_login'})
    with open('tests/fixtures/expected_empty_repo_list.json') as expected:
        expected_responce = json.loads(expected.read())
    assert responce.context['github_data'] == expected_responce


def test_repo_list():
    """Check responce if requested login exists and have repo(s)."""
    responce = client.get(TARGET_URL, {'github_login': 'ddh'})
    with open('tests/fixtures/expected_responce.json') as expected:
        expected_responce = json.loads(expected.read())
    assert responce.context['github_data'] == expected_responce
