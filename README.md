# Wazuh Telegram Integration

This project provides a custom integration for Wazuh to send alert notifications to a Telegram chat using a bot.

## Project Structure

- [`boni`](boni): Shell launcher script for the Python integration.
- [`boni_telegram.py`](boni_telegram.py): Python script that formats and sends Wazuh alerts to Telegram.
- [`ossec.conf`](ossec.conf): Example configuration for integrating the script with Wazuh.
- `README.md`: Project documentation.

---

## User Guide

### Prerequisites

- A working Wazuh server.
- A Telegram bot (created via [@BotFather](https://t.me/BotFather)) and your bot's API key.
- The chat ID where you want to receive alerts.

---

### 1. Install Dependencies

Install the required Python package on your Wazuh server:

```sh
pip install requests
```

### 2. Configure Wazuh Integration

Add the following to your `/var/ossec/etc/ossec.conf`:

```xml
<integration>
    <name>custom-telegram</name>
    <level>3</level>
    <hook_url>https://api.telegram.org/bot<API_KEY>/sendMessage</hook_url>
    <alert_format>json</alert_format>
</integration>
```

### 3. Set Up the Telegram Bot

1. Talk to [@BotFather](https://t.me/BotFather) on Telegram to create a new bot and get your API key.
2. Obtain your chat ID by messaging your bot and then visiting `https://api.telegram.org/bot<API_KEY>/getUpdates` to find your chat ID in the response.

### 4. Test the Integration

Generate a test alert in Wazuh and ensure it is received in your Telegram chat. Check the Wazuh logs for any errors related to the integration.