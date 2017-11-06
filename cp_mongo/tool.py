import cherrypy
import pymongo

__version__ = 0.1


class MongoTool(cherrypy.Tool):
    def __init__(self, **kw):
        cherrypy.Tool.__init__(self, 'on_start_resource',
                               self.on_start_resource,
                               priority=20)

    def _setup(self):
        cherrypy.Tool._setup(self)

    def on_start_resource(self, **kwargs):
        if not hasattr(cherrypy.request, "mongo") or \
           not getattr(cherrypy.request, "mongo"):
            args = {
                'host': 'localhost',
                'port': 27017,
                'max_pool_size': 10,
                'network_timeout': None,
                'tz_aware': False,
                'document_class': dict,
                '_connect': False
            }
            args.update(kwargs)
            connection = pymongo.Connection(**args)
            setattr(cherrypy.request, "mongo", connection)
        cherrypy.request.hooks.attach('on_end_resource', self.on_end_resource)

    def on_end_resource(self, **kwargs):
        if hasattr(cherrypy.request, "mongo") and getattr(cherrypy.request, "mongo"):
            c = getattr(cherrypy.request, "mongo").connection
            c.close()
            c.disconnect()
