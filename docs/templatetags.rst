#############
Template Tags
#############

.. highlightlang:: html+django

*********
util_tags
*********

safe
====

A wrapper for any other block tag to make the wrapped tag fail silently.

Usage::

    {% safe url view-name %}


**************
smart_humanize
**************

intsep
======

A clone of the Django default intcomma filter which takes an optional argument to
specify a character to use as seperator.

crop_empty_comma
================

Crops the digits after the decimal comma if they're equal to zero and optionally
replace it by the argument given.