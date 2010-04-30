#####
Views
#####

********************
utils.views.BaseView
********************

A base class to be used to build class based views. Don't worry too much about
how complicated the class looks. All you need to care about is the helper methods
to return responses and define a handle (and optionally handle_<request-method>) method.


Usage::

    class MyView(BaseView):
        allowed_methods = ['get']
        template = 'myapp/myview.html'
        
        def handle(self):
            return self.render_to_response({'user': self.request.user})
            
     my_view = MyView()