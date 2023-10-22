rsync -av --exclude /.git/ --exclude /README.md --exclude /.vscode --exclude /production/upload.sh --exclude __pycache__ --delete /home/mpeschel/projects/autocards/  autocards:/opt/sites/autocards
ssh -t autocards "sudo nginx -t && sudo nginx -s reload; sudo systemctl daemon-reload && sudo systemctl restart autocards && echo reloaded server ok"
