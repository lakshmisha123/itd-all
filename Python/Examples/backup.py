import os
import tarfile

def backup_directory(source_dir, backup_filename):
    with tarfile.open(backup_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

backup_directory('../Old', 'backup.tar.gz')
