---
layout: page
title: "Visual Studio Code - Personal Customizations"
categories:
  - Instructions
---

## Change color of multiline comments in Python 

Add this to your `settings.json`. The "foreground" key should have your color. This example is my desired color for Monokai Classic theme

```json
"editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "string.quoted.docstring.multi.python",
                "settings": {
                    "foreground": "#6E7066"
                }
            },
            {
                "scope": "string.quoted.docstring.multi.python punctuation.definition.string.end.python",
                "settings": {
                    "foreground": "#6E7066"
                }
            },
            {
                "scope": "string.quoted.docstring.multi.python punctuation.definition.string.begin.python",
                "settings": {
                    "foreground": "#6E7066"
                }
            }
        ]
    },
```

## Change the font for the Terminal

Add this to your `settings.json`. This is to fit a Oh-My-Zsh as your default shell tool

```json
"terminal.integrated.automationShell.linux": "",
"terminal.integrated.fontFamily": "Meslo LG M for Powerline",
```

## Vertical/Column Highlighting

Install [`cursoruler`](https://marketplace.visualstudio.com/items?itemName=freakone.cursoruler), and then paste the following in your `settings.json`. This example is specific to using Monokai Classic as the theme

```json
"cursor-ruler.color": "#32332D",
"cursor-ruler.width": "8px"
```