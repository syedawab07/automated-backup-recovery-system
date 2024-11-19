# Automated Backup and Recovery System

## Overview
This project demonstrates an **automated backup and recovery system** built using Linux Bash and Python. It performs scheduled backups of a source directory, applies a retention policy to delete old backups, and includes a recovery script for restoring files.

---

## Features
- **Automated Backups**: Compresses and stores backups using `tar`.
- **Retention Policy**: Deletes backups older than 7 days.
- **Recovery Script**: Allows restoring specific backups to a chosen directory.
- **Scheduling**: Automates backups using `cron`.

---

## Prerequisites
- Linux OS with Bash and Python 3 installed.
- Tools: `tar`, `cron`, and optionally `rsync` for advanced file transfer.

Install required tools:
```bash
sudo apt update
sudo apt install -y tar rsync python3
