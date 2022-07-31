import argparse
import ast
import json
import os
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
    print(os.environ.get("GIT_VARS"))
    print(type(os.environ.get("GIT_VARS")))
    GIT_VARS = ast.literal_eval(os.environ["GIT_VARS"])
    
    print(type(GIT_VARS))
    print(GIT_VARS)
    newDict = { key:value for (key,value) in GIT_VARS.items() if key in ["MY_SECRET_1"]}
    print(newDict)

    
else: 
    print ("File1 is being imported")