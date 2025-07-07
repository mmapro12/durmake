# durmake

**durmake** - Durpkg için otomatik pkgfile oluşturucu 

## Kurulum

Durmake'yi sisteminize kurmak için: 
```bash
git clone https://github.com/mmapro12/durmake.git 
cd durmake 
chmod +x ./install.sh
./install.sh
cd ..
rm -rf durmake 
```

Sistemden kaldırmak için: 
```bash 
sudo rm /usr/local/bin/durmake
```

## Kullanım

Durmake'yi anlayabilmeniz için ilk olarak durpkg ve pkgfile sistemini anlamanız gerekir. Bu bağlantıyı ziyaret ederek bunun hakkında gerekli tüm bilgilere erişebilirsiniz:
- [Durpkg github sitesi](https://github.com/mmapro12/durpkg)

Pkgfile kurulumunu başlatmak için:
```bash 
durmake 
```

Sonrasında ise size yönlendirilen soruları tam bir şekilde cevapladıktan sonra pkgfile'ınız bu dizinde bulacaksınız:
```bash
cd ./durmake/pkgfile.<paket-adı>.ini
```

Durpkg ve Pkgfile kurlumu hakkında daha fazla bilgi için:
- [Durpkg github sitesi](https://github.com/mmapro12/durpkg)


