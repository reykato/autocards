rsync -av --exclude /.git/ --exclude /README.md --exclude /production/upload.sh --delete /home/mpeschel/projects/autocards/  autocards:/opt/sites/autocards
ssh -t autocards "sudo systemctl daemon-reload && sudo systemctl restart autocards"
