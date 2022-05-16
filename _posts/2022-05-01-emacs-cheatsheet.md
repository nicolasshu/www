---
layout: article
title: "Emacs Cheatsheet"
tags:
  - Python
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
