#!/bin/bash

ACCESS_TOKEN=$(bash bash/get_token.sh | jq -r '.access_token')
HOMESERVER="https://matrix.agent.finances.tchap.gouv.fr"
TARGET_DISPLAY_NAME="Bot Client using Simple-Matrix-Bot-Lib"

# 1. Get devices with display_name equal to target name
DEVICE_IDS=$(curl -s -X GET \
  "$HOMESERVER/_matrix/client/v3/devices" \
  -H "Authorization: Bearer $ACCESS_TOKEN" | \
  jq -r --arg target "$TARGET_DISPLAY_NAME" \
  '.devices[] | select(.display_name == $target) | .device_id')

if [ -z "$DEVICE_IDS" ]; then
  echo "No device found with display name '$TARGET_DISPLAY_NAME'"
  exit 0
fi

