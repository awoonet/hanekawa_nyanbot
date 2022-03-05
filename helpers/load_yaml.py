import os, re, yaml


def load_yaml(path: str, message: str) -> dict:
    path = f"./static/{path}"
    yaml_files = os.listdir(path=path)

    result = {}

    counter = 0
    for file in yaml_files:
        key = file.split(".")[0]
        with open(f"{path}/{file}", "r") as file:
            file = file.read()
            file = re.sub("\t", "", file)
            value = yaml.load(file, Loader=yaml.Loader)
            counter += 1

        result[key] = value

    print(message.format(counter=counter), flush=True)

    return result
