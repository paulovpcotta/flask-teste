import logging
import traceback

from flask_restplus import Api
from sauron_telegram import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Documentação - Sauron Bot',
          description='APIs que o Bot possui contém')


@api.errorhandler
def default_error_handler(e):
    message = 'Um erro ocorreu.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
