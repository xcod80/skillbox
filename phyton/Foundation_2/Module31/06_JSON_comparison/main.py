import json

diff_list = ["services", "staff", "datetime"]
result = dict()
def cmpjson(jsold:dict, jsnew:dict):
    for key in jsold:
        if isinstance(jsold[key], dict):
            cmpjson(jsold[key], jsnew[key])
        if jsold[key] != jsnew[key] and key in diff_list:
            result[key] = jsnew[key]

with open('json_old.json', 'r') as file:
    jold = json.load(file)
with open('json_new.json', 'r') as file:
    jnew = json.load(file)

cmpjson(jold, jnew)
print(result)
with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)