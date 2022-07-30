import argparse
import yaml

def read_yaml(file):
    with open(file, "r") as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='SECRETS_ENV_VARS.')
    config = parser.add_argument('SECRETS_ENV_VARS',
                    help='secrets from github secrets')
    print(config.SECRETS_ENV_VARS)
else: 
    print ("File1 is being imported")