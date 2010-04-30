from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from django.contrib.auth import logout
from django.contrib.messages import debug, info, success, warning, error, add_message
from django.core.urlresolvers import reverse
from django.http import (
    HttpResponse, HttpResponseForbidden, Http404, HttpResponseNotAllowed,
    HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified,
    HttpResponseBadRequest, HttpResponseNotFound, HttpResponseGone,
    HttpResponseServerError
)
from utils.internal_utils import InternalRequest

class BaseView(object):
    """
    A base class to create class based views.
    
    It will automatically check allowed methods if a list of allowed methods are
    given. It also automatically tries to route to 'handle_`method`' methods if
    they're available. So if for example you define a 'handle_post' method and
    the request method is 'POST', this one will be called instead of 'handle'.
    
    For each request a new instance of this class will be created and it will get
    three attributes set: request, args and kwargs.
    """
    # A list of allowed methods (if empty any method will be allowed)
    allowed_methods = []
    # The template to use in the render_to_response helper
    template = 'base.html'
    # Only allow access to logged in users
    login_required = False
    # Only allow access to users with certain permissions
    required_permissions = []
    # Only allow access to superusers
    superuser_required = False
    # Response to send when request is automatically declined
    auto_decline_response = 'not_found'
    
    #===========================================================================
    # Dummy Attributes (DO NOT OVERWRITE)
    #=========================================================================== 
    request = None
    args = None
    kwargs = None
    
    #===========================================================================
    # Internal Methods
    #===========================================================================
    
    def __init__(self, *args, **kwargs):
        internal_request = kwargs.get('internal_request', None)
        if internal_request:
            internal_request.contribute_to_class(self)
        # Preserve args and kwargs
        self._initial_args = args
        self._initial_kwargs = kwargs

    @property
    def __name__(self):
        """
        INTERNAL: required by django
        """
        return self.get_view_name()
        
    def __call__(self, request, *args, **kwargs):
        """
        INTERNAL: Called by django when a request should be handled by this view.
        Creates a new instance of this class to sandbox 
        """
        if self.allowed_methods and request.method not in self.allowed_methods:
            return getattr(self, self.auto_decline_response)()
        if self.login_required and not request.user.is_authenticated():
            return getattr(self, self.auto_decline_response)()
        if self.superuser_required and not request.user.is_superuser:
            return getattr(self, self.auto_decline_response)()
        if self.required_permissions and not request.user.has_perms(self.required_permissions):
            return getattr(self, self.auto_decline_response)()
        handle_func_name = 'handle_%s' % request.method.lower()
        if not hasattr(self, handle_func_name):
            handle_func_name = 'handle'
        # Create a sandbox instance of this class to safely set the request, args and kwargs attributes
        sandbox = self.__class__(interal_request=InternalRequest(request, args, kwargs), *self._initial_args, **self._initial_kwargs)
        return getattr(sandbox, handle_func_name)()
    
    #===========================================================================
    # Misc Helpers
    #===========================================================================
    
    def get_view_name(self):
        """
        Returns the name of this view
        """
        return self.__class__.__name__
    
    def get_template(self):
        return self.template
    
    def logout(self):
        logout(self.request)
    
    #===========================================================================
    # Handlers
    #===========================================================================
    
    def handle(self):
        """
        Write your view logic here
        """
        pass
    
    #===========================================================================
    # Response Helpers
    #===========================================================================
    
    def not_allowed(self, data=''):
        return HttpResponseNotAllowed(data)
    
    def forbidden(self, data=''):
        return HttpResponseForbidden(data)
    
    def redirect(self, url):
        return HttpResponseRedirect(url)
    
    def named_redirect(self, viewname, urlconf=None, args=None, kwargs=None,
            prefix=None, current_app=None):
        return self.redirect(reverse(view, urlconf, args, kwargs, prefix, current_app))
    
    def permanent_redirect(self, url):
        return HttpResponsePermanentRedirect(url)
    
    def named_permanent_redirect(self, viewname, urlconf=None, args=None,
            kwargs=None, prefix=None, current_app=None):
        return self.permanent_redirect(reverse(view, urlconf, args, kwargs, prefix, current_app))
    
    def not_modified(self, data=''):
        return HttpResponseNotModified(data)
    
    def bad_request(self, data=''):
        return HttpResponseBadRequest(data)
    
    def not_found(self, data=''):
        return HttpResponseNotFound(data)
    
    def gone(self, data=''):
        return HttpResponseGone(data)
    
    def server_error(self, data=''):
        return HttpResponseServerError(data)
    
    def simplejson(self, data):
        return HttpResponse(simplejson.dumps(data), mimtype='application/json')
    
    def response(self, data):
        return HttpResponse(data)
    
    def render_to_response(self, data, request_context=True):
        if request_context:
            return render_to_response(self.get_template(), data, RequestContext(self.request))
        return render_to_response(self.get_template(), data)
    
    #===========================================================================
    # Message Helpers
    #===========================================================================
    
    def message_debug(self, message):
        debug(self.request, message)
        
    def message_info(self, message):
        info(self.request, message)
        
    def message_success(self, message):
        success(self.request, message)
        
    def message_warning(self, message):
        warning(self.request, message)
        
    def message_error(self, message):
        error(self.request, message)
        
    def add_message(self, msgtype, message):
        add_message(self.request, msgtype, message)