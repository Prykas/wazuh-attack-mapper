import json

def load_alerts(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        alerts = json.load(file)

    parsed = []

    for alert in alerts:

        parsed.append({
            "rule_id": alert["rule"]["id"],
            "description": alert["rule"]["description"],
            "groups": alert["rule"]["groups"],
            "agent": alert["agent"]["name"]
        })

    return parsed
