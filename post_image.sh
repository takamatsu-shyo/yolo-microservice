(echo -n '{"imageBase64": "'; base64 ~/Pictures/1.jpg; echo '"}') |
curl -H "Content-Type: application/json" -d @-  http://localhost:7777/resolution

