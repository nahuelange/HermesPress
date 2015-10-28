from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import RequestContext, loader
from hermes.models import RessourceCollection


def home(request):
    template = loader.get_template('hermes/home.html')

    context = RequestContext(request, {
        'collections': RessourceCollection.objects.all()
    })


    return HttpResponse(template.render(context))


def ressource_add(request, collection_id):
    collection = get_object_or_404(RessourceCollection, pk=collection_id)

    collection.add_ressource(request.POST.get('url'))

    return HttpResponseRedirect(reverse('home'))

def collection_add(request):
    pass

def collection(request, collection_id):
    collection = get_object_or_404(RessourceCollection, pk=collection_id)

    template = loader.get_template('hermes/collection.html')
    context = RequestContext(request, {
        'collection': collection
    })

    return HttpResponse(template.render(context))