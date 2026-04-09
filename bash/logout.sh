#!/bin/bash

# Configuration
ACCESS_TOKEN=$1
HOMESERVER="https://matrix.agent.finances.tchap.gouv.fr"
ENDPOINT="_matrix/client/v3/logout"

# Delete the specified device
delete_response=$(curl -X POST \
  "$HOMESERVER/$ENDPOINT" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{}')

