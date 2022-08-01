import argparse
import ast
import json
import os
from types import new_class
import yaml

def read_yaml(file):
    with open(file, "r") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__": 
    #parser = argparse.ArgumentParser(description='VERIFYING SECRETS_ENV_VARS FROM GITHUB.')
    #parser.add_argument('SECRETS_ENV_VARS',
    #                help='secrets from github secrets')

    #config = parser.parse_args()
    GIT_VARS = json.loads(os.environ.get("GIT_VARS") or '{}')
    print(GIT_VARS)
    newDict = { key:value for (key,value) in GIT_VARS.items() if key in ["MY_SECRET_5", "MY_SECRET_6"] }
    print(bool(newDict))
    print(type(newDict))
    print(len(newDict))
    if newDict:
        print(newDict)
    else: print("NOTHING")
else: 
    print ("File1 is being imported")