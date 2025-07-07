#!/bin/bash

source /venv/bin/activate
pyinstaller --onefile main.py 
sudo mv ./dist/main /usr/local/bin/durmake
sudo chmod +x /usr/local/bin/durkmake

echo "İndirme tamamlandı..."

