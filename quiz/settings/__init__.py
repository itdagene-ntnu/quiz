from quiz.settings import *

try:
    from quiz.settings.local import *
except ImportError, e:
    raise ImportError('Could not load local settings: quiz.settings' +
            '.local')
