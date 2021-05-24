from os import getenv

from dotenv import load_dotenv
from flask import Flask, request, Response

from text_ai import AIModule
from flask_pymongo import PyMongo
from pymongo.errors import *

from my_collections import User
import clicksend_client
from clicksend_client.rest import ApiException

import logging

logging.basicConfig(filename="logs.log", format='%(levelname)s:%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

load_dotenv()
app = Flask(__name__)
ai = AIModule()
app.config['MONGO_URI'] = getenv('MONGO_DOMAIN', 'mongodb://localhost:27017/myDatabase')
mongo = PyMongo(app)

configuration = clicksend_client.Configuration()
configuration.username = getenv('SMS_USER', 'mongodb://localhost:27017/myDatabase')
configuration.password = getenv('SMS_PASS', 'mongodb://localhost:27017/myDatabase')


def send_sms(name: str, contacts: list):
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))
    for contact in contacts:
        try:
            sms_message = clicksend_client.SmsMessage(source="safeher",
                                                      body=f"Your neighbor {name} is being attacked please call for help",
                                                      to=f"{contact.phone}")
            sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])
            api_response = api_instance.sms_send_post(sms_messages)
            #print(api_response)
        except ApiException as e:
            print("Exception when calling AccountApi->account_get: %s\n" % e)
    pass


def call_neighbor():
    pass


def call_police():
    pass


def perform_action(user: User):
    # last_call = datetime(user.last_call())
    # Todo: pull user info from mongodb
    # Todo: add check last call
    # Todo: Check preferred communication method in compere the known history
    send_sms(name=f"{user.full_name()}", contacts=user.emergency_contacts)
    pass


def load_user(data: dict):
    user_id = data.get('Owner', ' ')
    try:
        user = mongo.db.users.find_one({'id': user_id})
        if user:
            user = User(doc=user)
        return user
    except ServerSelectionTimeoutError:
        print("Server is incorrect")
        return None
    except ExecutionTimeout:
        print("Execution time was too long")
        return None
    except:
        print('Unknown Error')
        return None


def create_user(data: dict):
    user = User(doc=data)
    try:
        mongo.db.users.insert_one(user.to_dict())
    except ServerSelectionTimeoutError:
        print("Server is in-correct")
    except ExecutionTimeout:
        print("Excution too long")
    except:
        print('Unknown Error')
        raise


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/register', methods=['POST'])
def register():
    create_user(request.json)
    return Response(status=200)


@app.route('/api/analysis', methods=['POST'])
def hardware_post():
    logging.info(f"post from hardware")
    j = request.json
    if request.is_json:
        logging.info(f"the device {j} made call to server")
        user = load_user(j['device'])
        if user:
            logging.info(f"The user {user.full_name()} with the {j.get('device',{}).get('SSID','')}")
            sen = j.get('sentence')
            logging.info(f'the next text was sent {sen}')
            (ans, pre) = ai.predict_value(sen)
            if ans >= 0.5 or user.safe_word in sen and user.safe_word != '':
                print("----" * 5)
                print("this text has aggressive vibe")
                print("----" * 5)
                print("send SMS")
                print("----" * 5)
                perform_action(user)
            else:
                print('this text has a natural vibe')
    return "OK"


if __name__ == '__main__':
    print("----" * 5)
    print("Server backend")
    print("----" * 5)

    port = getenv('PORT', 5555)
    logging.info(f"Server has started at port {port}")
    app.run(port=port)
