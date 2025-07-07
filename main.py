import subprocess

print("durmake: otomatik pkgfile oluşturucu script")

name = input("Paketin adı nedir? ")
author = input("paketin yazarı kimdir? ")
version = input("Paketin versiyonu nedir? (format: X.Y.Z) ")
description = input("Paketin kısa özeti: ")
helpc = input("Paketin yardım komutu nedir? ")
helpw = input("Paketin yardım sayfası veya wikisi nedir? ")
source = input("Paketin kod kaynağı web sitesi: (github olsun) ")
install_type = input("Paket .deb dosyası ile mi kurulacak yoksa bir script ile mi? (deb/script)")
deb_source = ""
if install_type == "deb":
    deb_source = input("Paketin .deb kaynağı nedir? (.deb ile biten url olsun) ")

setup = input("Paketi kurmadan önce bir komuta ihtiyaç var mı? Varsa komutu yazınız yoksa boş bırakınız: ")
needs = int(input("paketin install scripti için kod kaynağına ihityaç var mı? (0/1) "))
install = input("paketin install scriptini yazınız: (kaynak kodun içindeymiş gibi yazınız) ")
config = input("paketi kurduktan sonra bir yapılandırmaya ihtiyacınız varsa komutu yazınız: ")

print ("paket oluşturuluyor...")
pkgfile = f"""
[package]
name = {name}
author = {author}
version = {version}
description = {description}
source = {source}
needs = {needs}
install_type = {install_type}
deb_source = {deb_source} 
help_command = {helpc}
help_page = {helpw}

[scripts]
setup = {setup}
install = {install}
config = {config}
"""

subprocess.run(["mkdir", "-p", "durmake"], check=True)
with open(f"./durmake/pkgfile.{name}.ini", "w") as f:
    f.write(pkgfile)

print(f"paket oluşturuldu.\n\t\t{name}: ./durmake/pkgfile.{name}.ini")


