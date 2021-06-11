from django.shortcuts import (
    render
)


def homePageView(request):
    context = {
    }
    return render(request, 'index.html', context)