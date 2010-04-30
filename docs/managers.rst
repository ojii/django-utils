########
Managers
########

*************************
utils.manager.BaseManager
*************************

A subclass of `django.db.models.Manager` which adds two additional methods.

BaseManager.get_or_none
=======================

Returns an object for the lookup arguments given or `None`.

BaseManager.get_or_404
======================

Return an object for the lookup arguments given or raises a `Http404` Exception.