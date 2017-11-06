import os

import cherrypy

from cp_mongo import MongoTool

HERE = os.path.dirname(os.path.abspath(__file__))


class Root(object):

    @property
    def mongo(self):
        return cherrypy.request.mongo

    def page(self):
        return '''
        <html>
          <head><title>CherryPy-SQLAlchemy Example</title></head>
          <body>
            <form action='/' method='post'>
              <input type='text' name='message' /><input type='submit' value='add' />
            </form>
            %s
          </body>
        <html>
        '''

    @cherrypy.expose
    def index(self, message=None, submit=None):
        if message:
            self.mongo.ExampleCollection.insert_one({'message': message})
            raise cherrypy.HTTPRedirect('/')

        page = self.page()

        ol = ['<ol>']
        for msg in self.mongo.ExampleCollection.find({}):
            ol.append('<li>%s</li>' % msg['message'])
        ol.append('</ol>')

        return page % ('\n'.join(ol))


def run():
    cherrypy.tools.mongo = MongoTool()

    app_config = {
        '/': {
            'tools.mongo.on': True,
            'tools.mongo.collection': 'ExampleCollection'
        }
    }
    cherrypy.tree.mount(Root(), '/', config=app_config)

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    run()
