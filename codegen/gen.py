import json

if __name__ == "__main__":
    with open("apis.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for k, v in data.items():
        if v["definition"]["code"] != 0:
            continue
        else:
            print(
                f"{v['meta']['Project']}/{v['meta']['Version']}/{v['meta']['Name']}_{v['meta']['Resource'].replace('.','_')}"
            )
