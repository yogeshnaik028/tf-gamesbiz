# This is the file that implements a flask server to do inferences. It's the file that you will modify to
# implement the scoring for your own algorithm.

from __future__ import print_function

import json

import flask


class ScoringService(object):
    model = None

    @classmethod
    def get_model(cls):

        cls.model = 1
        return cls.model


app = flask.Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():

    health = ScoringService.get_model() is not None

    status = 200 if health else 404
    return flask.Response(response='\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():

    data = None

    if flask.request.content_type == 'application/json':
        data = flask.request.data.decode('utf-8')
        # s = StringIO.StringIO(data)
        # data = pd.read_csv(s, header=None)
    else:
        return flask.Response(response='This predictor only supports JSON data', status=415, mimetype='text/plain')

    print('Invoked with {} records'.format(data.shape[0]))

    result = {str(type(data)): json.dumps(data)}

    return flask.Response(response=json.dumps(result), status=200, mimetype='application/json')