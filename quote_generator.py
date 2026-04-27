#cli program that randomly generates a quote
import random



# new_quote = "yes"

# while new_quote.lower() in ["yes", "y"]:

# A dictionary of quotes.
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