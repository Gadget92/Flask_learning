import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 'ouyrg$&7p-1)f@76vdqr9@da$figdarq292^45eh7%85(je**y'
