# Gallerist

Discord bot built with Py3 and bs4 to display the object of the day from the **SAINT LOUIS ART MUSEUM**

ref : <https://www.slam.org/explore-the-collection/object-of-the-day/>

``` Py

Workflow

1. bot to listen for command
2. deploy webscrapper to ref site
    2.1 Download image locally
    2.2 Formulate the description and metadata details regarding the object
3. and return the object of the day *with details* (optional)

```

## Usage 

1. Clone repo into local machiene 
2. Set up Discord application and bot following Discord [docs](https://discordpy.readthedocs.io/en/stable/discord.html)
3. Copy token from discord bot created and edit place into the env variable in the .env file
4. Run `python3 bot.py`

## Commands

Two commands are supported:

1. !gallerist


2. !help <command>

``
    Returns description of the command
``
