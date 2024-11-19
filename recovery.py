import os
import tarfile

# Variables
BACKUP_DIR = "/demo/backup"
RESTORE_DIR = "/demo/source_data_restore"

# Ensure directories exist
if not os.path.exists(BACKUP_DIR):
    print(f"Backup directory not found: {BACKUP_DIR}")
    exit(1)

if not os.path.exists(RESTORE_DIR):
    os.makedirs(RESTORE_DIR)

# List available backups
print("Available backups:")
backups = [f for f in os.listdir(BACKUP_DIR) if f.endswith(".tar.gz")]
if not backups:
    print("No backups available!")
    exit(1)

for idx, backup in enumerate(backups):
    print(f"{idx + 1}: {backup}")

# Select a backup to restore
choice = int(input("\nEnter the number of the backup to restore: ")) - 1
if choice < 0 or choice >= len(backups):
    print("Invalid choice!")
    exit()

# Restore the selected backup
backup_file = os.path.join(BACKUP_DIR, backups[choice])
print(f"Restoring {backup_file} to {RESTORE_DIR}...")

with tarfile.open(backup_file, "r:gz") as tar:
    tar.extractall(path=RESTORE_DIR)

print("Restore completed successfully.")
