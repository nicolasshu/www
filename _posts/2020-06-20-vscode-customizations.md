---
layout: page
title: "Visual Studio Code - Personal Customizations"
categories:
  - Instructions
---

## Useful Plugins
- [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2)
- [cursoruler](https://marketplace.visualstudio.com/items?itemName=freakone.cursoruler)
- [Kite Autocomplete for Python and JavaScript](https://marketplace.visualstudio.com/items?itemName=kiteco.kite)
- [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) and/or [Live Share Extension Pack](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)
- [Render Line Endings](https://marketplace.visualstudio.com/items?itemName=medo64.render-crlf)
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
- [vscode-icons](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)

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
"cursor-ruler.width": "8px",
```

## Remove Tooltip/Suggestions
Add the following to your JSON settings

```json
"editor.parameterHints": false,
```