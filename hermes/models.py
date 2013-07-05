from django.db import models
from hermes.extractor import TermExtractor
import httplib2

class RessourceManager(models.Manager):
    def create_ressource(self, url):
        try:
            ressource = self.get(url=url)
            raise Exception
        except Ressource.DoesNotExist:
            ressource = Ressource(url=url)

        extractor = TermExtractor(url)
        ressource.title = extractor.get_title()
        ressource.excerpt = extractor.get_excerpt()
        ressource.save()

        for term in extractor.get_terms():
            ressource.tags.add(Tag.objects.get_or_create(name=term)[0])

        return ressource


class Tag(models.Model):
    name = models.CharField(max_length=255)

class Ressource(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name='ressources')
    excerpt = models.TextField()

    objects = RessourceManager()

