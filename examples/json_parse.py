import urllib.request
import urllib.parse
import json
import ast
import pprint
import re


def get_data_from_url(base_url, parameters):
    """
    Function gets base url and parameters as dictionary, sends request and returns data as json file.
    """
    params = urllib.parse.urlencode(parameters)
    url = base_url + params
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        data = response.read()
        data = data.decode("utf-8")
        json.loads(data)
    return data


if __name__ == "__main__":
    base_url = "https://en.wikipedia.org/w/api.php?"
    parameters = {"action": "parse",
                  "page": "Henry_VIII_of_England",
                  "format": "json"}
    data = get_data_from_url(base_url, parameters)
    data = ast.literal_eval(data)
    print(data.keys())
    for key in data['parse'].keys():
        print(key, type(data['parse'][key]))
    print(data['parse']['text'].keys())
    # print(data['parse']['text']['*'])
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data['parse']['text'])
    print()
    text = re.search(r'Father.+?title="(.+?)">', data['parse']['text']['*'])
    print('Father:', text.group(1))
