#!/bin/bash

# Start ngrok in the background and log its output to ngrok.log
nohup ngrok http 5005 --log=stdout > ngrok.log &
# Sleep for a few seconds to give ngrok time to start
sleep 5

# Extract the ngrok URL from ngrok.log and remove "url=" prefix
ngrok_url=$(cat ngrok.log | grep "https://" | awk '{print $8}' | sed 's/url=//')

# Ensure the URL has /webhooks/telegram/webhook at the end
ngrok_url_with_path="$ngrok_url/webhooks/telegram/webhook"

# Update the credentials.yml file with the ngrok URL
sed -i "s|webhook_url: .*|webhook_url: \"$ngrok_url_with_path\"|g" credentials.yml

# Start the Rasa actions server
nohup rasa run actions --actions actions &

# Start the Rasa server with your model and enable API
nohup rasa run -m models --enable-api --cors "*"
