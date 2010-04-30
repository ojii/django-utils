from django.db.models.fields import CharField
from utils.internal_utils import AutoSlugFieldFiller


class AutoSlugField(CharField):
    __AUTO_SLUG_FIELD_SIGNALS = {}
    
    def __init__(self, connected_to, verbose_name=None, name=None,
        max_length=None, unique=False, blank=False, null=False,
        db_index=False, db_column=None, db_tablespace=None, only_fill_once=True):
        """
    def __init__(self, verbose_name=None, name=None, primary_key=False,
            max_length=None, unique=False, blank=False, null=False,
            db_index=False, rel=None, default=NOT_PROVIDED, editable=True,
            serialize=True, unique_for_date=None, unique_for_month=None,
            unique_for_year=None, choices=None, help_text='', db_column=None,
            db_tablespace=None, auto_created=False):
        """
        self.connected_to = connected_to
        self.only_fill_once = only_fill_once
        super(AutoSlugField, self).__init__(verbose_name, name, False, max_length,
            unique, blank, null, db_index, None, '', False, True, unique_for_date,
            unique_for_month, unique_for_year, None, '', db_column, db_tablespace,
            False)
        
    def get_internal_type(self):
        return "AutoSlugField"

    def contribute_to_class(self, cls, name):
        super(AutoSlugField, self).contribute_to_class(cls, name)
        if not cls in AutoSlugField.__AUTO_SLUG_FIELD_SIGNALS:
            AutoSlugField.__AUTO_SLUG_FIELD_SIGNALS[cls] = {}
        if not name in AutoSlugField.__AUTO_SLUG_FIELD_SIGNALS[cls][name]:
            AutoSlugField.__AUTO_SLUG_FIELD_SIGNALS[cls][name] = AutoSlugFieldFiller(cls, name, self)