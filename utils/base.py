from django.core.urlresolvers import reverse, NoReverseMatch

def reverse(viewname, urlconf=None, args=None, kwargs=None, prefix=None, current_app=None, default=''):
    """
    A 'safe' reverse method which either returns the URL or a given default.
    """
    try:
        return reverse(viewname, urlconf, args, kwargs, prefix, current_app)
    except NoReverseMatch:
        return default