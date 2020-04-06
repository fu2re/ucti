import csv

from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


from ucti.echo import Echo


@csrf_exempt
def index_view(request):
    """
    Simplest possible streaming response from django docs
    """
    rows = (["Row {}".format(idx), str(idx)] for idx in range(999999))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response


@csrf_exempt
def redirect_view(request, depth: int):
    """
    Minimum depth is 2.
    """
    if depth <= 1:
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('multiple', kwargs={
        'depth': depth-1
    }))


@csrf_exempt
def infinite_view(request):
    return HttpResponseRedirect(reverse('infinite'))
