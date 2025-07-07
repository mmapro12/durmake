#!/bin/bash

source ./venv/bin/activate
pyinstaller --onefile main.py 
sudo cp ./dist/main /usr/local/bin/ 
sudo chmod +x /usr/local/bin/durmake

echo "İndirme tamamlandı..."

