from django.db.models import Manager
from django.http import Http404


class BaseManager(models.Manager):
    """
    A Manager with a few extra helper methods
    """
    def get_or_none(self, *args, **kwargs):
        """
        Returns an object for given lookup arguments or None.
        """
        try:
            return self.get(*args, **kwargs)
        except self.model.DoesNotExist:
            return None
        
    def get_or_404(self, *args, **kwargs):
        """
        Returns an object for given lookup arguments or raises a 404.
        """
        obj = self.get_or_none(*args, **kwargs)
        if not obj:
            raise Http404
        return obj