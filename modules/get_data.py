import urllib.request
import urllib.parse
import json
import ast
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


def get_information(page):
    """
    Parses information from web-page and returns dict with all needed information.
    :param page: str
    :return: dict
    """
    base_url = "https://en.wikipedia.org/w/api.php?"
    parameters = {"action": "parse",
                  "page": page,
                  "format": "json"}
    data = get_data_from_url(base_url, parameters)
    data = ast.literal_eval(data)
    try:
        data = data['parse']['text']['*']
        name = " ".join(page.split("_"))
        try:
            born = re.search(r'Born.+?(\d{3,4})<', data).group(1)
        except AttributeError:
            born = "NI"
        try:
            died = re.search(r'Died.+?(\d{3,4})', data).group(1)
        except AttributeError:
            if born == "NI":
                died = "NI"
            else:
                died = "present"
        reg = re.compile(r'Spouse.+?Issue', re.DOTALL)
        text = reg.findall(data)
        reg = re.compile(r'.+?title="([A-Z].+?)">', re.DOTALL)
        partner_names = reg.findall(str(text))
        reg = re.compile(r'Issue.+?/Dynasty', re.DOTALL)
        text = reg.findall(data)
        reg = re.compile(r'.+?title="([A-Z].+?)">', re.DOTALL)
        children_names = reg.findall(str(text))
        try:
            father = re.search(r'Father.+?title="(.+?)">', data).group(1)
            mother = re.search(r'Mother.+?title="(.+?)">', data).group(1)
        except AttributeError:
            try:
                father = re.search(r'Parents.+?title="(.+?)".+?father', data).group(1)
                mother = re.search(r'Parents.+?father.+?title="(.+?)".+?mother', data).group(1)
            except AttributeError:
                father = None
                mother = None
    except KeyError:
        name = " ".join(page.split("_"))
        born = "NI"
        died = "NI"
        partner_names = []
        children_names = []
        father = None
        mother = None
    return {"name": name, "born": born, "died": died, "partner_names": partner_names, "children_names": children_names,
            "father": father, "mother": mother}

