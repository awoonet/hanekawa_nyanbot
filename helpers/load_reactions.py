import os, re, yaml


def load_reactions() -> dict:
    path = "./static/reactions"
    reactions_yaml = os.listdir(path=path)

    reactions = {}

    for reaction in reactions_yaml:
        key = reaction.split(".")[0]
        with open(f"{path}/{reaction}", "r") as file:
            file = file.read()
            file = re.sub("\t", "", file)
            value = yaml.load(file, Loader=yaml.Loader)

        reactions[key] = value

    print("Reactions loaded.")

    return reactions
