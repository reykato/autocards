rsync -av --exclude /.git/ --exclude /README.md --exclude /.vscode --exclude /production/upload.sh --exclude __pycache__ --delete /home/mpeschel/projects/autocards/  autocards:/opt/sites/autocards
ssh -t autocards "sudo systemctl daemon-reload && sudo systemctl restart autocards"
