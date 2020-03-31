import urllib.request
import urllib.parse
import json


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
    parameters = {"action": "query",
                  "list": "search",
                  "srsearch": "king",
                  "format": "json"}
    data = get_data_from_url(base_url, parameters)
    print(data)
