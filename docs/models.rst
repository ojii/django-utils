######
Models
######

****************************
utils.modes.slugify_uniquely
****************************

Returns a unique slug from a string.

The `base` argument should be a string to be slugified. `model` is the model this
slug has to be unique for the field defined by `slug_field`.

An example if you want to uniquely slugify a `title` field on an instance::

    slugify_uniquely(instance.slugify, instance.__class__)
    
   
***************************
utils.models.field_distinct
***************************

This method is *slow* and does *not* return a queryset like one might expect, it
rather returns a generator which yields objects distinct for a field.