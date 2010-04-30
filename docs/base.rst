##############
Base Utilities
##############

******************
utils.base.reverse
******************

The purpose of this function is to provide a silently failing way to reverse a
URL.

The syntax is exactly the same as the standard Django `django.core.urlresolvers.reverse`
function, except that it takes an extra keyword argument `default` which will be
returned if no reverse match can be found.