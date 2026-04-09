ACCESS_TOKEN=$(echo "$(bash get_token.sh)" | jq -r '.access_token')
MATRIX_HOMESERVER="https://matrix.agent.finances.tchap.gouv.fr"
ENDPOINT="_matrix/client/v3/rooms/$ROOM_ID/send/m.room.message/\$event_id?access_token=$ACCESS_TOKEN"
ROOM_ID=$TCHAP_ROOM_ID


# Envoi du message
curl -X PUT \
  "$MATRIX_HOMESERVER/$ENDPOINT" \
  -H "Content-Type: application/json" \
  -d '{
    "msgtype": "m.text",
    "body": "'"$MESSAGE"'"
  }'

# source logout.sh $ACCESS_TOKEN
