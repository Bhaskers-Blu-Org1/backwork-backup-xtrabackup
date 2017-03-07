#!/usr/bin/env bash
ts=`date +%Y%m%d%H%M%S`
backup_path="/tmp/backups/$ts"
backup_file="/tmp/backups/$ts.tar.gz"
mkdir -p $backup_path

monsoon backup xtrabackup --target-dir=$backup_path
tar -czf $backup_file $backup_path
monsoon upload softlayer -u IBMOS283639-9:laoqui -p 2be1a8f8eabf4c1f690a956e524be4999f4d67d4826f18eeb0cecc00174cd344 -d tor01 -c BDU_RANCHER_NA $backup_file $ts

echo "Cleaning up"
rm -fr $backup_path $backup_file
