ACCESS_TOKEN=$(echo "$(bash get_token.sh)" | jq -r '.access_token')
HOMESERVER="https://matrix.agent.finances.tchap.gouv.fr"
ROOM_ID=$TCHAP_ROOM_ID
EVENT_ID="\$02fYR2Uw-cyqSPkJdaSXTS9hZAgIGjIMPcMOWuJk_7Q"
ENDPOINT="_matrix/client/v3/rooms/$ROOM_ID/event/$EVENT_ID?access_token=$ACCESS_TOKEN"

curl -X GET "$HOMESERVER/$ENDPOINT" \
-H "Content-Type: application/json" \
-d '{}'

source logout.sh $ACCESS_TOKEN
