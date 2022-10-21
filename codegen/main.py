import json

import httpx

dict_apis = {}


def get_catalog():
    catalog = httpx.get("https://open.feishu.cn/api_explorer/v1/api_catalog").json()
    with open("catalog.json", "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False)


def get_api_definition(api_identity):
    definition = httpx.get(
        "https://open.feishu.cn/api_explorer/v1/api_definition", params=api_identity
    ).json()
    return definition


def get_nested_api_summary(data):
    if data.get("apiSummary"):
        if not data["apiSummary"]["debuggable"]:
            return

        if data["apiSummary"].get("apiIdentity"):
            api_identity = data["apiSummary"]["apiIdentity"]
            key: str = f"{api_identity['project']}.{api_identity['version']}.{api_identity['resource']}.{api_identity['apiName']}"

            dict_apis[key] = data["apiSummary"]
            definition = get_api_definition(api_identity)
            dict_apis[key]["definition"] = definition
        else:
            print(data)

    if isinstance(catalog := data.get("children"), list):
        if "历史版本" in data["name"]:
            return

        for child_catalog in catalog:
            get_nested_api_summary(child_catalog)


if __name__ == "__main__":
    get_catalog()

    with open("catalog.json", "r", encoding="utf-8") as f:
        items = json.load(f)["data"]["items"]

    for item in items:
        get_nested_api_summary(item)
        with open("apis.json", "w", encoding="utf-8") as f:
            json.dump(dict_apis, f, ensure_ascii=False, indent=2)
