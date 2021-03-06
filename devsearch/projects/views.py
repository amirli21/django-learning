from django.shortcuts import render



projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]






def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects':projectsList}
    return render(request, 'projects/projects.html',context=context)

# same as in the urlpatterns, in the path function's first argument
def project(request, pk):
    return render(request, 'projects/single_project.html', context={'parameter':pk})

