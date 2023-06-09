# Daily Protocol

This repo contains 
- the [collection of all daily protocols](protocols)
- a folder with all the [slides of the bootcamp](slides)
- [group work results](group_work)
- [code for creating random groups](pairing/random_groups.py)
- a folder to store some helpful [cheatsheets](cheatsheets)

## Create a new daily protocol

Please write your daily protocol in **markdown format** (*.md). This is a nice way to have a formatted text on github. In the [daily protocol template](protocols/protocol_template.md) you can see the basic structure of the protocol and some tips on formatting text in markdown as well as how to add pictures or gifs.
Please also read the [How to contribute](#how-to-contribute) part, which explains how to add your work to this repository. Please add new protocols to the [protocols folder](protocols).

## How to contribute

To contribute to this repository, please create a **new branch** and add your work there. Open a **pull request** and ask one of your colleagues to **review** your work. You need at least one approval to **merge** your work into the main branch. Once you have merged your branch, please also **delete the branch** to maintain a clean repository.

## How to create random groups

Open a terminal and run:

```bash
 python pairing/random_groups.py
 ```

In line 24 of the [random_groups python script](pairing/random_groups.py) is the participants list. Add all participants names there.

 **Prerequisites: Python 3.**
You can check out your python version with 
```bash
python --version
```
