#! /bin/bash

mysqldump --all-databases --user=root --password=***** > all-databases-backup.sql

current_date=$(date +%Y%m%d)
backupdir=/tmp/mysqldumps/$current_date

mkdir -p $backupdir

mv all-databases-backup.sql $backupdir

