from django.shortcuts import (
    render
)


def blogOverview(request):
    context = {
    }
    return render(request, 'overview.html', context)