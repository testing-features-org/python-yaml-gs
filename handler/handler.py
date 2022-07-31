import argparse
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
    
    print(os.environ["GIT_VARS"])
else: 
    print ("File1 is being imported")