Random Quote CLI

A simple, lightweight command‑line program that prints a randomly selected quote from a curated list of John Piper sayings. Run it once, get one quote — no prompts, no loops, no configuration. Designed for quick inspiration directly from your terminal.
Features
Prints a single random quote on each execution
Zero dependencies beyond Python’s standard library
Easy to extend with more authors or quotes
Clean, minimal, one‑file design
Installation
Clone or download the project files to your machine.
No packages or setup steps are required.
Usage

Run the script with Python:
bash
python quote_generator.py

Example output:
Code
It is better to lose your life than to waste it.
-John Piper

How It Works
The script:
Stores quotes as (author, text) tuples in a list
Uses Python’s random.choice() to select one
Prints the quote text and author to the console
This keeps the program extremely fast and easy to modify.

Code Overview
python
import random

quotes = [
    ("John Piper", "God is most glorified in us when we are most satisfied in Him."),
    ("John Piper", "One of the great uses of Twitter and Facebook will be to prove at the Last Day that prayerlessness was not from lack of time."),
    ("John Piper", "If you don't feel strong desires for the manifestation of the glory of God, it is not because you have drunk deeply and are satisfied. It is because you have nibbled so long at the table of the world. Your soul is stuffed with small things, and there is no room for the great."),
    ("John Piper", "If you live gladly to make others glad in God, your life will be hard, your risks will be high, and your joy will be full."),
    ("John Piper", "What is sin? It is the glory of God not honored. The holiness of God not reverenced. The greatness of God not admired. The power of God not praised. The truth of God not sought. The wisdom of God not esteemed. The beauty of God not treasured. The goodness of God not savored. The faithfulness of God not trusted. The commandments of God not obeyed. The justice of God not respected. The wrath of God not feared. The grace of God not cherished. The presence of God not prized. The person of God not loved. That is sin."),
    ("John Piper", "Christ did not die to forgive sinners who go on treasuring anything above seeing and savoring God. And people who would be happy in heaven if Christ were not there, will not be there. The gospel is not a way to get people to heaven; it is a way to get people to God. It's a way of overcoming every obstacle to everlasting joy in God. If we don't want God above all things, we have not been converted by the gospel."),
    ("John Piper", "It is better to lose your life than to waste it."),
    ("John Piper", "Grace is the pleasure of God to magnify the worth of God by giving sinners the right and power to delight in God without obscuring the glory of God."),
    ("John Piper", "Grace is the pleasure of God to magnify the worth of God by giving sinners the right and power to delight in God without obscuring the glory of God."),
    ("John Piper", "Missions is not the ultimate goal of the church. Worship is. Missions exists because worship doesn't.")
]

quote = random.choice(quotes)
author, text = quote
print(text)
print(f"-{author}")
Customization
You can expand the quote list by adding more entries:
python
quotes.append(("New Author", "Your new quote here."))
Or explore enhancements like:
adding_categories
supporting_multiple_authors
adding_command_line_flags
creating_a_loop_mode

Project Structure
Code
.
├── quote_generator.py
└── README.md

License
This project is free to use, modify, and share.
