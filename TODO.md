

Previous printCard
```python
def printCard(card: Card):
    # This function will print a card in a formatted way

    #     This section will take a string of abilities and format it into lines of 50 characters
    #     with a "| "  at the beginning of each line
    #     The section avoid splitting words in the middle and will instead move the whole word to the next line.
    abilities_formatted = ""
    words = card.abilities.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) <= 60:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    abilities_formatted = "\n".join([f"| {line}" for line in lines])

#    This section will print the card
    print(
        f"---  {card.name}\n"
        f"| C: {card.cost}, {'inkable, ' if card.inkable else ''}{card.color.value}"
    )
    match card.card_type:
        case CardType.CHARACTER:
            print(
                f"| S: {card.strength}, W: {card.willpower}, L: {card.lore}\n"
                f"| {', '.join([c.value for c in card.classifications])}"
            )
        case CardType.LOCATION:
            print(f"| M: {card.moveCost}, W: {card.willpower}, L: {card.lore}")
        case CardType.ITEM:
            print("| Item")
        case CardType.ACTION:
            print("| Action")
        case CardType.SONG:
            print("| Action/Song")
    print(abilities_formatted)
    print("---")
```