from gql import gql
from gql.client import Client
from gql.transport.requests import RequestsHTTPTransport

from gh_repos.settings.common import GH_API_TOKEN

GH_API_URL = 'https://api.github.com/graphql'


class GraphQLError(Exception):
    """GraphQLError Exception."""

    def __init__(self, message):
        """Init Network Exception.

        Args:
            message (str): message error
        """
        self.message = message


def fetch_owner_data(login):
    """Fetch data about owner from GITHUB API."""
    transport = RequestsHTTPTransport(
        GH_API_URL,
        headers={'Authorization': 'Bearer {0}'.format(GH_API_TOKEN)},
    )

    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Provide a GraphQL query
    query = gql(
        """
        query getRepos($login: String!) {
            user(login: $login) {
                login
                name
            }
        repositoryOwner(login: $login) {
            repositories(first:100)
                {
                    nodes {
                        name
                        stargazers {
                            totalCount
                    }
                }
            }
        }
    }
    """)
    query_vars = {'login': login}
    try:
        return client.execute(query, query_vars)
    except Exception as error:
        return str(error)
