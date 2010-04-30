from django.db.models.signals import pre_save

class AutoSlugFieldFiller(object):
    def __init__(self, model, fieldname, field):
        self.model = model
        self.fieldname = fieldname
        self.field = field
        pre_save.connect(self.fill, sender=model)
        
    def fill(self, instance, **kwargs):
        if getattr(instance, self.fieldname) and self.field.only_fill_once:
            return
        from utils.models import slugify_uniquely
        value = slugify_uniquely(self.field.connected_to, self.model, self.fieldname,
            self.field.max_length)
        setattr(instance, self.fieldname, value)
        
        
class InternalRequest(object):
    def __init__(self, request, args, kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        
    def contribute_to_class(self, cls):
        cls.request = self.request
        cls.args = args
        cls.kwargs = kwargs