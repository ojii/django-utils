from django.template.defaultfilters import slugify

def slugify_uniquely(base, model, slug_field='slug', max_length=255, slugifier=slugify,
         extra_queryset_kwargs={}):
    """
    Returns a unique slug for a given model and slug field.
    The base is the string to slugify.
    You may define a custom slugifier function if the default django one does not
    suite your needs.
    """
    i = 0
    slug = slugifier(base)[:max_length]
    while model.objects.filter(**extra_queryset_kwargs).filter(**{slug_field:slug}).count():
        postfix = str(i)
        i += 1
        slug = slugifier(base)[:max_length - len(postfix)] + postfix
    return slug

def field_distinct(qs, field):
    """
    WARNING: SLOW!!!
    """
    cash = []
    for obj in qs:
        val = getattr(obj, field)
        if val not in cash:
            cash.append(val)
            yield obj