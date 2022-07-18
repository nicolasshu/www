---
layout: article
title: "Python on Emacs"
permalink: /python_on_emacs.html
---

There are many people who like to use [elpy](https://github.com/jorgenschaefer/elpy) or [ein](https://github.com/millejoh/emacs-ipython-notebook) to use Python on Emacs. RealPython even makes a [blog post](https://realpython.com/emacs-the-best-python-editor/) which is actually quite useful to get Python up and running on Emacs. However, there's an even better package which is called [emacs-jupyter](https://github.com/nnicandro/emacs-jupyter). It really brings the feel from the VSCode's [Python Interactive mode](https://code.visualstudio.com/docs/python/jupyter-support-py#_python-interactive-window).

# Installing 
In order to install it, you may follow the instructions on the [emacs-jupyter](https://github.com/nnicandro/emacs-jupyter) repository. At the time of this writing, they say that you may simply install the package `jupyter` via the `package-install`. I.e. `M-x package-install RET jupyter RET`

If you are using Spacemacs, you may install it by adding it to `dotspacemacs-configuration-layers` > `dotspacemacs-additional-packages`. 

```elisp 
dotspace-configuration-layers '(
    ...
    dotspacemacks-additional-packages '(
        ...
        jupyter
        ...
    )
)
```

Then, you can run `SPC-f e R` to reload your configuration file. 


# Usage

In order to use the package, first you will need to initiate a Python interpreter which contains the `ipykernel` package. If your kernel does not show up on Jupyter environments, you can run the following command as documented [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html#kernels-for-different-environments). 

```bash
source activate myenv
python -m ipykernel install --user --name myenv --display-name "Python 3 (myenv)"
```

By default, the commands which evaluate lines or regions will send the outputs to the a minibuffer. If you'd like it to be sent to the REPL that you will initialize, add the following to your config file (e.g. `dotspacemacs/user-config` in Spacemacs)

```elisp
(setq jupyter-repl-echo-eval-p t)
```

First open up a new Python file. 
![](../assets/images/python_in_emacs/step1.png)

In order to initiate a Python interpreter, run the command `M-x jupyter-run-repl`. This will initialize a new buffer containing the REPL. 

![](../assets/images/python_in_emacs/step2.png)

Next, back to your Python file, you must associate this buffer with the REPL that you have just started. In order to do so, run `M-x jupyter-repl-associate-buffer`, and then select the buffer that you have just started. 

![](../assets/images/python_in_emacs/step3.png)

You can start to then run the lines of code. By default, you will have `C-c C-c` to send the current line of code (or region) to the REPL. 

![](../assets/images/python_in_emacs/step5.png)

To create a region, you may also set a mark using `C-SPC`, and then move your cursor to wherever you'd like your region to extend. This will allow you to run the `M-x jupyter-eval-region`.

![](../assets/images/python_in_emacs/step6.png)

You may also set up a keybinding to your Emacs config (in Spacemacs, it will be on `dotspacemacs/user-config`) to your `jupyter-eval-region` command. 

```elisp
(global-set-key (kbd "C-c C-x") 'jupyter-eval-region)
```

# Making the Marker Visible

You may also make the marker visible. Taking the code used in the [EmacsWiki](https://www.emacswiki.org/emacs/MakingMarkVisible), which it's shown below, you may add it to your config file (e.g. `dotspacemacs/user-config`). 

```elisp
;;;; Make the mark visible, and the visibility toggleable. ('mmv' means 'make
;;;; mark visible'.) By Patrick Gundlach, Teemu Leisti, and Stefan.

(defface mmv-face
  '((t :background "maroon2" :foreground "white"))
  "Face used for showing the mark's position.")

(defvar-local mmv-mark-overlay nil
  "The overlay for showing the mark's position.")

(defvar-local mmv-is-mark-visible t
  "The overlay is visible only when this variable's value is t.")

(defun mmv-draw-mark (&rest _)
  "Make the mark's position stand out by means of a one-character-long overlay.
   If the value of variable `mmv-is-mark-visible' is nil, the mark will be
   invisible."
  (unless mmv-mark-overlay
    (setq mmv-mark-overlay (make-overlay 0 0 nil t))
    (overlay-put mmv-mark-overlay 'face 'mmv-face))
  (let ((mark-position (mark t)))
    (cond
     ((null mark-position) (delete-overlay mmv-mark-overlay))
     ((and (< mark-position (point-max))
           (not (eq ?\n (char-after mark-position))))
      (overlay-put mmv-mark-overlay 'after-string nil)
      (move-overlay mmv-mark-overlay mark-position (1+ mark-position)))
     (t
      ; This branch is called when the mark is at the end of a line or at the
      ; end of the buffer. We use a bit of trickery to avoid the higlight
      ; extending from the mark all the way to the right end of the frame.
      (overlay-put mmv-mark-overlay 'after-string
                   (propertize " " 'face (overlay-get mmv-mark-overlay 'face)))
      (move-overlay mmv-mark-overlay mark-position mark-position)))))

(add-hook 'pre-redisplay-functions #'mmv-draw-mark)

(defun mmv-toggle-mark-visibility ()
  "Toggles the mark's visiblity and redraws it (whether invisible or visible)."
  (interactive)
  (setq mmv-is-mark-visible (not mmv-is-mark-visible))
  (if mmv-is-mark-visible
      (set-face-attribute 'mmv-face nil :background "maroon2" :foreground "white")
    (set-face-attribute 'mmv-face nil :background 'unspecified :foreground 'unspecified))
  (mmv-draw-mark))

(global-set-key (kbd "C-c v") 'mmv-toggle-mark-visibility)
```

As you can see, the keybinding `C-c v` toggles the visibility of the marker. Alternatively, if you wish to keep your configuration file cleaner, you may add it to a different file, and load it in your config file. 

```elisp
(add-to-list 'load-path "/path/to/parent/directory/of/makemarkvisible.el")
(load "makemarkvisible.el")
```

The final results can be shown below. 

![](../assets/images/python_in_emacs/step7.png)

