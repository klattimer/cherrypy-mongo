import cherrypy
from pymongo import MongoClient

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
                "uri": "mongodb://localhost:27017",
                "database": "ExampleDatabase"
            }
            args.update(kwargs)
            client = MongoClient(args['uri'])
            setattr(cherrypy.request, "_mongo_client", client)
            setattr(cherrypy.request, "mongo", client[args['database']])
        cherrypy.request.hooks.attach('on_end_resource', self.on_end_resource)

    def on_end_resource(self, **kwargs):
        if hasattr(cherrypy.request, "mongo") and getattr(cherrypy.request, "mongo"):
            c = getattr(cherrypy.request, "_mongo_client")
            c.close()
            setattr(cherrypy.request, "_mongo_client", None)
            setattr(cherrypy.request, "mongo", None)
