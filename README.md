# Render the Website

```bash
bundle exec jekyll serve
```

# Guide to Customizing

## Customizing Name, Theme, Comments, etc

This theme contains a lot of different ways to customize your site with plugins and many other things. It's truly a great theme. A lot of this customization can be found at `_config.yml`. There are too many things to cover, but here are a few:
```yaml
url    :     {This should be your domain name. E.g. http://namesurname.com}
title:       {The title that will show on your website}
description: {The description that will show when you hover over the mouse over the title}
mathjax:     {whether it will have MathJax}
mermaid:     {whether it will allow for Mermaid}
paginate:    {The number of items that will be on your home page}
```

## Adding a Item to Header

Once you create an `*.md` file on root, it will create a file at `_site/*.html`. This file will be important. Next, go to the file `_data/navigation.yml` and add another `- title` entry to the list. E.g. 


```
header:
  .
  .
  .

  - titles:
      # @start locale config
      en      : &EN       Name_of_Item
      en-GB   : *EN
      en-US   : *EN
      en-CA   : *EN
      en-AU   : *EN
      zh-Hans : &ZH_HANS  Name_in_CN
      zh      : *ZH_HANS
      zh-CN   : *ZH_HANS
      zh-SG   : *ZH_HANS
      zh-Hant : &ZH_HANT  
      zh-TW   : *ZH_HANT
      zh-HK   : *ZH_HANT
      ko      : &KO       
      ko-KR   : *KO
      fr      : &FR       Name_in_FR
      fr-BE   : *FR
      fr-CA   : *FR
      fr-CH   : *FR
      fr-FR   : *FR
      fr-LU   : *FR
      # @end locale config
    url: /CV.html
```

So, all you have to do is to update that Markdown file and it will be created once you reload the `bundle jekyll exec serve`

## Creating New Skins

In order to create new screens, you should create new `*.scss` files at 
- `_sass/skins/` for a theme
- `_sass/skins/highlight/` for a highlighting theme

This can then can be changed later at `_config.yml`

## Layouts of Posts and Pages

In order for articles and posts layouts, please go to their main guide [here](https://tianqi.name/jekyll-TeXt-theme/samples.html)

### Sidebars

This took a little while for me to get it down. In order to get a functioning layout, make sure that you have a layout name (e.g. `guide_to_fool`), and in the name of your article, add the front matter below. Additionally, it's helpful to have a permalink to your page.

```yaml
---
permalink: /page/fooling_a_boss.html
sidebar:
    nav: guide_to_fool
---
```

Several of your articles will ideally have that same `sidebar` front matter. Next, on the file `_data/navigation.yml`, add a new navigation group. This will have a display title in `title`, and subsections in `children`. So you can do something like:

```yaml
guide_to_fool:
    - title: A Guide to Fool Others
    children: 
        - title: Fooling Your Boss
          url: /page/fooling_a_boss.html
        - title: Fooling Your Family
          url: /page/fooling_family.html
        - title: Fooling Your S.O.
          url: /page/fooling_so.html
```

## Font Change

In order to change your global font, add the `*.ttf` file to `assets/fonts`, and add the following to the file `_sass/custom.scss`

```scss
@font-face {
    font-family: "{Font Name}";
    src: url("../fonts/{filename}.ttf");
  }
```

Next, go to the file `_sass/common/_variables.scss`, and go to `$base` > `font-family`. There will be several name fonts within parenthesis. This is set as a fallback, so that if the browser is unable to show the first one, then it moves on to the next one, and repeats. So, simply add the font to the beginning as such:

```scss
$base: (
  font-family:            ("{Font Name}", sans-serif, "Segoe UI", -apple-system, BlinkMacSystemFont, Helvetica, Arial),
  ...
)
```


## Activating it through Github Pages

On your domain provider add 
- Type: CNAME Record
- Host: www
- Value/IP Address: nicolasshu.github.io