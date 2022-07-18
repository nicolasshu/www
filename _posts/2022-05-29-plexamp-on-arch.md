---
layout: article
title: "Plexamp on Arch"
permalink: /plexamp_on_arch.html
---


So it turns out that Plexamp is a little buggy, and installing it from the AUR is not guaranteed to work. Instead, you can install it via [Flatpak](https://flathub.org/apps/details/com.plexamp.Plexamp). 

```bash
flatpak install flathub com.plexamp.Plexamp
```

Once that is installed you can run it via
```bash
flatpak run com.plexamp.Plexamp
```

However, you may not always want to have to type it all out on a terminal, and it is not found by default on Rofi, for example. So Flatpak applications are usually found in `/var/lib/flatpak/app/`. Moreover, at the time of this writing, Plexamp can be found here:

```bash
/var/lib/flatpak/app/com.plexamp.Plexamp/
```

Its `.desktop` file can be therefore found here
```bash
/var/lib/flatpak/app/com.plexamp.Plexamp/x86_64/stable/active/export/share/applications/com.plexamp.Plexamp.desktop
```

Therefore, what you can then do is:
```bash
cp /var/lib/flatpak/app/com.plexamp.Plexamp/x86_64/stable/active/export/share/applications/com.plexamp.Plexamp.desktop ~/.local/share/applications
```

And after you copy it there, you'll start to find it via Rofi
