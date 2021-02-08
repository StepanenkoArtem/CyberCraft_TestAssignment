from django.shortcuts import render

from repos import github


def parse(response):
    """Parse JSON data obtained from GitHub."""
    if isinstance(response, str):
        return {
            'github_owner': None,
            'error': response,
        }

    owner = {}
    owner['login'] = response.get('user').get('login')
    owner['name'] = response.get('user').get('name')
    owner['nodes'] = []
    for node in response.get('repositoryOwner')['repositories']['nodes']:
        owner['nodes'].append(
            {
                'name': node['name'],
                'stars': node['stargazers']['totalCount'],
            },
        )
    return {
        'github_owner': owner,
        'error': None,
    }


def repo_list(request, *args, **kwargs):
    """Return dict contains Github repo owner name and his repos."""
    if request.GET.get('github_login'):
        github_responce = github.fetch_owner_data(
            request.GET.get('github_login'),
        )
        context = parse(github_responce)
    else:
        context = {}

    return render(
        request=request,
        template_name='repos.html',
        context=context,
    )
