#!/usr/bin/env python
#!/bin/sh
# Wazuh Python script launcher
# Author : Boni Yeamin
# Date : 2025-06-30
#Email : boniyeamin.cse@gmail.com

import sys
import json
import requests
from requests.auth import HTTPBasicAuth

# Replace with your actual chat ID
CHAT_ID = "8122757062"

# Read configuration parameters
alert_file = open(sys.argv[1])
hook_url = sys.argv[3]

# Read the alert file
alert_json = json.loads(alert_file.read())
alert_file.close()

# Extract data fields
rule_id = alert_json['rule']['id'] if 'id' in alert_json['rule'] else "N/A"
alert_level = alert_json['rule']['level'] if 'level' in alert_json['rule'] else "N/A"
description = alert_json['rule']['description'] if 'description' in alert_json['rule'] else "N/A"
agent = alert_json['agent']['name'] if 'name' in alert_json['agent'] else "N/A"
timestamp = alert_json['timestamp'] if 'timestamp' in alert_json else "N/A"
srcip = alert_json.get('data', {}).get('srcip', "N/A")
user = alert_json.get('data', {}).get('user', "N/A")

# Map Wazuh alert level to severity
def get_severity(level):
    try:
        level = int(level)
    except Exception:
        return "Unknown"
    if level >= 15:
        return "Critical severity"
    elif 12 <= level <= 14:
        return "High severity"
    elif 7 <= level <= 11:
        return "Medium severity"
    elif 0 <= level <= 6:
        return "Low severity"
    else:
        return "Unknown"

severity = get_severity(alert_level)

# Compose the message in the desired format
message = (
    f"🚨 AG SOC Alert 🚨\n"
    f"🆔 Rule ID: `{rule_id}`\n"
    f"⚠️ Alert Level: `{alert_level}`\n"
    f"🔴 Severity: {severity}\n"
    f"🖥 Agent: `{agent}`\n"
    f"📝 Description: {description}\n"
    f"🕒 Time: {timestamp}\n"
    f"🌐 Source IP: {srcip}\n"
    f"👤 User: {user}\n"
    f"\n✍️ Author: Infosec Team"
)

# Prepare data to send
msg_data = {
    'chat_id': CHAT_ID,
    'text': message,
    'parse_mode': 'Markdown'  # Enables bold, italic, code formatting
}

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

# Send the request
requests.post(hook_url, headers=headers, data=json.dumps(msg_data))

sys.exit(0)