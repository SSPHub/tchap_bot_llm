HOMESERVER="https://matrix.agent.finances.tchap.gouv.fr"
ENDPOINT="_matrix/client/v3/login"

curl -X POST "$HOMESERVER/$ENDPOINT" \
-H "Content-Type: application/json" \
-d '{
    "type": "m.login.password",
    "password": "'"$TCHAP_BOT_SSPHUB_PWD"'",
    "identifier": {
        "type": "m.id.user",
        "user": "'"$TCHAP_BOT_SSPHUB_MATRIX_ID"'"
    },
    "device_id": "API"
}'
