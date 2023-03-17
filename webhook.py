import web
import logging


urls = (
    '/payload','payload'
)
app = web.application(urls, globals())
logging.basicConfig(level=logging.DEBUG,
                    filename='webhook.log',
                    filemode='a',
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    )
class payload:
    def verify(self,input):
        logging.debug(input)
        return True

    def executeScript(self):
        pass

    def POST(self):
        input = web.input()
        if self.verify(input):
            self.executeScript()
        else:
            return "invalidRequest"

if __name__ == "__main__": app.run()
