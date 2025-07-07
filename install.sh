#!/bin/bash

source ./venv/bin/activate
pyinstaller --onefile durmake.py 
sudo cp ./dist/durmake /usr/local/bin/ 
sudo chmod +x /usr/local/bin/durmake

echo "İndirme tamamlandı..."

