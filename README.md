# nu2gallery

![GitHub](https://img.shields.io/github/license/gonvalhector/nu2gallery)
![GitHub contributors](https://img.shields.io/github/contributors/gonvalhector/nu2gallery?logoColor=orange)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/gonvalhector/nu2gallery)
![GitHub issues](https://img.shields.io/github/issues-raw/gonvalhector/nu2gallery)

![nu2gallery's logo](https://lh3.googleusercontent.com/pw/AJFCJaXNpON4f5ERH4Mmb3Maxw1D9Fz5Zti3ogODMlkygwP2Y_zNim2cd-xN5zAV8ujhd9BrRpqNKttJF69Ay-ihtPl6lUTm3rQaBF20Uon_I7FD7vcCK-eMLecR0IFro9Vsfcv8jTqgkDNerGNGpHc2PdYk=w1200-h630-s-no?authuser=0 "nu2gallery's logo")

## Introduction

**nu2gallery** is a Python tool that writes a new *Markdown* file with metadata necessary to display an image post for [gonvalhector.github.io](https://github.com/gonvalhector/gonvalhector.github.io).  
The [site](https://www.gonvalhector.com) utilizes [Jekyll](https://jekyllrb.com/) as its *Static Site Generator*, which uses MD files with [Front Matter](https://jekyllrb.com/docs/front-matter/) for its posts. Image posts, as I implemented them for the gallery, contain many variables in its *front matter* that are then used by a template to display them as HTML pages.  
There was a lot of time-consuming copy-pastying used in the first few image posts I made for the site, so I ended up writing a little Python program that would streamline that process.  
That program became outdated and hard to update when newer features were implemented for the image posts, so writing a similar tool that could be easily updated, mantained and expanded upon turned into a priority. This became **nu2gallery**.

## Table of Contents

- [Technologies/Requirements](#technologies--requirements)
- [Usage](#usage)
- [Credits](#credits)

## Technologies / Requirements

Python 3.4+

## Usage

At the command prompt, type `python3 nu2gallery.py` and follow the prompts.

## Credits

### Owner / Mantainer

[Hector Gonzalez](https://github.com/gonvalhector)

### Contributors

[zubayer hossain](https://github.com/zubu007)