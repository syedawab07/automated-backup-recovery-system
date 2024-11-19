#!/bin/bash

# Variables
SOURCE_DIR="/demo/source_data"
BACKUP_DIR="/demo/backup"
LOG_FILE="$BACKUP_DIR/backup.log"
DATE=$(date +%Y-%m-%d_%H-%M-%S)

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Perform backup with tar
BACKUP_FILE="$BACKUP_DIR/backup_$DATE.tar.gz"
tar -czf $BACKUP_FILE $SOURCE_DIR

# Log the result
if [ $? -eq 0 ]; then
    echo "[$(date)] Backup successful: $BACKUP_FILE" >> $LOG_FILE
else
    echo "[$(date)] Backup failed!" >> $LOG_FILE
    exit 1
fi

# Delete backups older than 7 days
find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +7 -exec rm {} \;

echo "Backup process completed."
