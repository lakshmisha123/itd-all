#!/bin/bash

# URL of the file to be downloaded
FILE_URL="$1"

# Destination where the file will be saved
DEST_FILE="$2"

# Download the file using wget
wget -O "$DEST_FILE" "$FILE_URL"

# Check if the file was successfully downloaded
if [[ -f "$DEST_FILE" ]]; then
  # Display the size of the file using 'du' in human-readable format
  FILE_SIZE=$(du -h "$DEST_FILE" | cut -f1)
  echo "Downloaded file size: $FILE_SIZE"
else
  echo "Failed to download the file."
fi