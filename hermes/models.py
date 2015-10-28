from django.db import models
from django.template import Context, loader

from metadata_parser import MetadataParser
from pyembed.core import PyEmbed
from pyembed.core.consumer import PyEmbedConsumerError


class RessourceManager(models.Manager):
    def get_or_create_ressource(self, url):
        try:
            ressource = self.get(url=url)
            raise Exception
        except Ressource.DoesNotExist:
            ressource = Ressource(url=url)

            md_strategy = ['og', 'dc', 'page', 'meta', ]
            md = MetadataParser(url=url)

            ressource.title = md.get_metadata('title', )
            ressource.excerpt = md.get_metadata('description', )
            ressource.image = md.get_metadata('image', )

        ressource.save()

        return ressource

    def get_last(self):
        return self.all().order_by('-date')[:5]


class Tag(models.Model):
    name = models.CharField(max_length=255)

class RessourceCollection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def add_ressource(self, url):
        ressource = Ressource.objects.get_or_create_ressource(url)
        if ressource:
            ressource.collection.add(self)
            ressource.save()

class Ressource(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='ressources')
    excerpt = models.TextField(null=True)
    collection = models.ManyToManyField(RessourceCollection, related_name='ressources')
    image = models.URLField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    objects = RessourceManager()


    def render(self):
        template = loader.get_template('hermes/render_ressource.html')
        context = Context({
            'ressource': self,
        })
        try:
            html = PyEmbed().embed(self.url)
            context['oembed'] = html
        except PyEmbedConsumerError:
            pass
        return template.render(context)