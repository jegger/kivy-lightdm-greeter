#About
This is a simple greeter for LightDM based on Kivy.
I guess this is nothing for production, just a demonstration what can be made.

![ScreenShot](https://raw.github.com/jegger/kivy-lightdm-greeter/master/screenshot.png)

#Requirements
- Deb packages: liblightdm-gobject-1-0 gir1.2-lightdm-1 python-gobject
- And of course Kivy


#Installation
1. Assure you are using as lightDM as your login-manager
2. cp kivy-greeter.py /usr/local/bin/
3. cp kivy-greeter.desktop /usr/share/xgreeters/
4. make sure kivy-greeter is executable: chmod +x /usr/local/bin//kivy-greeter.py
5. Activate the kivy-greeter: open /etc/lightdm/lightdm.conf and append/change: greeter-session=kivy-greeter
6. reboot or ```initctl restart lightdm```


#Debuging
```lightdm --test-mode --debug``` => kivy logs are in: $HOME/.cache/lightdm/log/x-1-greeter.log


#Credits / More information
http://www.mattfischer.com/blog/?p=5
