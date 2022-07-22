---
layout: article
title: "Emacs Cheatsheet"
tags:
  - emacs
permalink: /emacs_cheatsheet.html
---

These are a few things to remember about Emacs

# Adding a Path

In order to add a path to your Emacs config file, you can write the following

```
(add-to-list 'load-path "~/path/to/dir")
```

If you are using Doom Emacs, you should then add this to the `config.el` file. For example, if you wish to add the [org-bullets](https://github.com/sabof/org-bullets) package, once you've saved the `org-bullets.el` file somewhere (e.g. `~/path/to/emacs_packages`), you can add 

```
;; To add to the path
(add-to-list 'load-path "~/path/to/dir")

;; Add Org-Bullets to the emacs configuration
(require 'org-bullets)
(add-hook 'org-mode-hook (lambda () (org-bullets-mode 1)))
```

Source: https://www.emacswiki.org/emacs/LoadPath

# Changing the Splash screen

In order to change the splash screen, you can add 

```
(setq fancy-splash-image "~/path/to/image.png")
```

If you are using Doom Emacs, you'll put this on your `config.el` file. 


# Relative Line Numbering

If you'd like there to be a relative line numbering on your Emacs text editors, you can set the following:

```
(setq display-line-numbers-type 'relative)
```


# Spacemacs
## Adding a package 
In order to add a custom package, you'll quickly realize that there are specific rules to follow, and using `M-x package-insta RET <name_of_package>` will work for the current session, however, once you restart Spacemacs, it will be deleted. So, if you look at the documentation, you need to look into your `~/.spacemacs` file, and there it says that 

> Spacemacs will only install the packages that are explicitly used by the user. A package is considered to be used if its layer is used (i.e. listed in `dotspacemacs-configuration-layers`). Any packages that are not used is considered to be orphan and is deleted at the next startup of Emacs.

But it isn't super clear at first where you're actually supposed to put. At first, when you go to `dotspacemacs/layers`, what I initially tried was to put it my packages under `dotspacemacs-configuration-layers`, but that didn't necessarily work

```lisp
(defun dotspacemacs/layers ()
    (setq-default 
        ...
        dotspacemacs-configuration-layers
        '(emacs-lisp
          helm
          treemacs
          ...
          doom-themes ; Try doing this
        )
        
    )
)
```

However, instead, if you put it on `dotspacemacs-additional-packages`, it will start to work!
```lisp
(defun dotspacemacs/layers ()
    (setq-default 
        ...
        dotspacemacs-configuration-layers
        '(emacs-lisp
          helm
          treemacs
        )
        dotspacemacs-additional-packages 
        '(
          rainbow-mode
          doom-themes
        )
    )
)
```

However, when putting it there, you'll need to also do some modifications on your `dotspacemacs/user-config`

```lisp
(defun dotspacemacs/user-config()
    (load-theme 'doom-one)
)
```

But theming is something that will not work with Spacemacs, as it needs a specific customization. By doing this, you'll need to authorize to use the theme every single time you use it. Instead, you'll need to go to `dotspacemacs/init` and add it to `dotspacemacs/themes`
