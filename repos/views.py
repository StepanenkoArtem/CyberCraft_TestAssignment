from django.shortcuts import render


# Create your views here.
def repo_list(request, *args, **kwargs):
    """Return dict contains Github repo owner name and his repos."""
    github_data = {
        'github_login': 'ArtemStepanenko',
        'github_owner_name': 'Artem Stepanenko',
        'github_repos': [
            {'name': 'first', 'stars': 24},
            {'name': 'second', 'stars': 54},
            {'name': 'third', 'stars': 28},
        ],
    }
    return render(
        request,
        template_name='repos.html',
        context={'github_data': github_data},
    )
