from django import template
from django.template.defaulttags

register = template.Library()

class SafeNode(template.Node):
    def __init__(self, real_node):
        self.real_node
        
    def render(self, context):
        try:
            return self.real_node.render(context)
        except:
            return ""

def safe(parser, token):
    """
    A tag to surpress errors raised in other tags.
    
    Usage:
    
        {% safe real-tag-name real-tag-args %}
        
    Example:
    
        {% safe url view_name %}
        
        translates into
        
        {% url view_name %} 
        
        but will not raise an exception if no reverse is found.
    """
    token.contents.lstrip('safe ')
    bits = token.split_contents()
    try:
        real_func = parser.tags[bits[0]]
    except KeyError:
        raise template.TemplateSyntaxError("Invalid block tag '%s'" % bits[0])
    real_node = real_func(parser, token)
    return SafeNode(real_node)