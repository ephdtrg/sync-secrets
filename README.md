## Installation
---

### Clone repository
```
$ git clone https://github.com/ephdtrg/sync-secrets.git
```

### Setup sync path

Export backup path to shell variable
For example:
```
export BACKUP_DIR = '/home/user/backup'
```

### Generate script and install

```
make
make install
```

## Usage
---
```
$ sync-secrets filename.txt
```

File will be saved at configured directory with path, relative to home directory, or absolute path in other cases

For example, if backup directory is `/home/user/backup`, 
file `/home/user/foo/bar.txt` will be saved at `/home/user/backup/foo/bar.txt`

Multiple file copying is supported, but directory copying is untested.

Next update may bring simple versioning.
