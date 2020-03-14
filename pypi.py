import requests
import json
import ast

from pathlib import Path

if Path('requirement.txt').is_file():
    print ("File exist")

    try:
        with open('requirement.txt') as f:
            x = f.readlines()
            toFind=x[4]
            # print(type(toFind))
            print(toFind)
            data = requests.get("https://pypi.org/pypi/{}/json".format(toFind))

            raw_json = data.content

            a = json.loads(raw_json.decode('utf-8'))
            print(a['info']['description'])
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)



else:
    print ("File not exist")