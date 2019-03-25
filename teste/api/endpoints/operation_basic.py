import logging

from flask import Flask
from flask import request
from flask_restplus import Resource, Api 
from sauron_telegram.api.restplus import api
from sauron_telegram.api.endpoints.bot_sauron import send_message
from sauron_telegram.api.endpoints.bot_sauron import send_message_image
from sauron_telegram.api.endpoints.bot_sauron import transform_image

log = logging.getLogger(__name__)

ns = api.namespace('endpoints/posts', description='Post operação.')

TOKEN = "637217321:AAFqSw0KJnwpbhm3upF4qcCAHpxjPn6n_fQ"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

@ns.route('/')
class PostsCollection(Resource):

    def get (self):
        return "teste"

    @api.response ( 200, 'Enviado para o bot Sauron.' )
    def post (self):
        objSauron = request.json
        send_message(objSauron['message'], objSauron['chat_id'])
        send_message_image(objSauron['chat_id'], transform_image(objSauron['photo']))
        return None , 200