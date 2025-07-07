# Wazuh Telegram Integration

This project provides a custom integration for Wazuh to send alert notifications to a Telegram chat using a bot.

## Project Structure

- [`boni`](boni): Shell launcher script for the Python integration.
- [`boni_telegram.py`](boni_telegram.py): Python script that formats and sends Wazuh alerts to Telegram.
- [`ossec.conf`](ossec.conf): Example configuration for integrating the script with Wazuh.
- `README.md`: Project documentation.

## Setup Instructions

### 1. Configure Wazuh Integration

Add the following to your `/var/ossec/etc/ossec.conf`:

```xml
<integration>
    <name>custom-telegram</name>
    <level>3</level>
    <hook_url>https://api.telegram.org/bot<API_KEY>/sendMessage</hook_url>
    <alert_format>json</alert_format>
</integration>