---
layout: article
title: "Github and SSH Keys"
tags:
  - Python
permalink: /github_ssh.html
---

This is a guide to add a SSH key to your Github account. 

A good guide is done by Antonio Medeiros [here](https://linuxkamarada.com/en/2019/07/14/using-git-with-ssh-keys/) and [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

# Existing SSH Keys

First, check and see what are the current SSH keys. This can be done with 

```bash
$ ls -lah ~/.ssh

total 28K
drwx------  2 nickshu nickshu 4.0K Dec 21 00:45 .
drwx------ 45 nickshu nickshu 4.0K Jan 13 15:00 ..
-rw-------  1 nickshu nickshu 4.2K Dec 29 21:14 known_hosts
-rw-------  1 nickshu nickshu 3.5K Dec 21 00:39 known_hosts.old
```

# Generate a new SSH Key

Next, you need to generate a new key. If you check the `man ssh-keygen`, you'll see that the `-t` tag has 6 different types of keys you can choose from. 

- DSA
- EcDSA
- EcDSA-SK
- Ed25519
- Ed25519-SK
- RSA

For more information on some of these types, you may visit https://goteleport.com/blog/comparing-ssh-keys/

```bash
$ ssh-keygen -t ed25519 -C "username@email.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/username/.ssh/id_ed25519): 
```

Here you may either enter a specific path for your key pair, or you may use the default location. Finally, you will 
be prompted to enter a password.

```
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
```

This will create a key pair: a private and a public key on your desired location. The public key will have the extension `.pub`, whereas the private key will not have an extension. Do not share your private key. 

# Add the Key to Github

On Github, go to your `Settings` > `SSH and GPG keys`, where you will see a list of your SSH keys.

Press on `New SSH key` and copy and paste your SSH public key (e.g. /home/username/.ssh/mykey.pub). 

At this point, the key has been added to your Github account. Now you need to add it to the `ssh-agent`. 

# Add your SSH Key to the ssh-agent

## One-Time Use

Your SSH agent will help you so that you are not having to add your passphrase every time. First start the ssh-agent in the background.

```bash
$ eval "$(ssh-agent -s)"
```

Next, add the SSH private key to the ssh-agent. 

```bash
$ ssh-add ~/.ssh/path/to/ssh/private/key
```

## Permanent Use

So, the easiest way to do so is to force the keys to be always kept. This can be done by adding to the `~/.ssh/config` file. If your file does not exist, then simply create it and add the private keys

```
IdentityFile ~/.ssh/github_priv_key
IdentityFile ~/.ssh/server_priv_key
```

And then change the permissions to 600

```bash
$ cd ~/.ssh
$ ls -la
...
-rw-r--r-- 1 nickshu nickshu   58 Jan 13 16:01 config
...

$ chmod 600 ~/.ssh/config
$ ls -la
...
-rw------- 1 nickshu nickshu   58 Jan 13 16:01 config
...
```

Alternatively, if you'd like to map a specific key to a specific host, you may use the following:

```
Host github.com
    User git
    IdentityFile ~/.ssh/github_priv_key
```

Finally, from this point on, you won't have to add the SSH key to the SSH agent every time. A more thorough answer can be found [here](https://stackoverflow.com/a/4246809)

# Test your SSH connection

```
$ ssh -T git@github.com
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```
