#!/bin/bash

# Get the learning text from the first argument, or use the last git commit message
LEARNING_TEXT=${1:-$(git log -1 --pretty=%B)}

# Get the webhook URL
WEBHOOK_URL=$(cat discord-webhook)

# Get the current date
DATE=$(date +"%B %d, %Y")

# Fixed values for now
TIME_SPENT="2.5 hours"
WORD_OF_THE_DAY="**Automation:** The use of technology to perform a process or procedure with minimal human assistance."

# Construct the message content, ready for JSON (with \n for newlines)
MESSAGE_CONTENT="Hi Fellows,\n\nToday's Update:\n\nDate: $DATE\nTime Spent: $TIME_SPENT\n\nWord of the day: $WORD_OF_THE_DAY\n\nLearning of the Day: $LEARNING_TEXT"

# Escape quotes in the learning text just in case
MESSAGE_CONTENT_ESCAPED=$(echo "$MESSAGE_CONTENT" | sed 's/"/\"/g')

# Create the JSON payload
JSON_PAYLOAD="{\"content\": \"$MESSAGE_CONTENT_ESCAPED\"}"

# Send the update to Discord using curl
curl -X POST -H "Content-Type: application/json" -d "$JSON_PAYLOAD" "$WEBHOOK_URL"
