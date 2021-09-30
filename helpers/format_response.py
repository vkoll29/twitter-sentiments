import json
import ast


def formatted_response(json_response):
    """
    Format tje json response from twitter into the documents shape expected by azure. Only extract the data from response and create a dictionary
    whose key is called documents. Then create a json formatted str which is then deserialized. return an ast literal_eval result of the deserialized str
    :param json_response: response from twitter's recent search endpoint
    :return: evaluated json string
    """
    data = json_response['data']
    doc_start = '"documents": {}'.format(data)
    str_json = '{' + doc_start + '}'
    dump_doc = json.dumps(str_json)
    doc = json.loads(dump_doc)
    return ast.literal_eval(doc)