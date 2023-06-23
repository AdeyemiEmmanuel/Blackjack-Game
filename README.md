# Blackjack-Game
Welcome to the Blackjack Game project! This is a simple implementation of the popular card game Blackjack, also known as 21, using Python.

## Introduction

The Blackjack Game project is a command-line based application that allows you to play the classic card game of Blackjack against the computer. It provides an interactive and engaging experience where you can test your luck and strategy against the dealer. The game supports multiple players, allowing you to compete against your friends or family.

The project is implemented in Python and utilizes basic object-oriented programming concepts to model the game's components, such as the deck of cards, players, and the dealer. The game logic follows the standard rules of Blackjack.

## Game Rules

Blackjack is a card game where the goal is to have a hand value closer to 21 than the dealer's hand value without exceeding 21. Here are some key rules of the game:

- The cards have the following values: numbered cards (2-10) are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces are worth either 1 or 11.
- At the beginning of each round, you and the dealer are dealt two cards each. One of the dealer's cards remains hidden.
- Players take turns making decisions for their hands, such as requesting additional cards (hit) to increase their hand value or choosing to stop taking cards (stand).
- If a player's hand value exceeds 21, they bust and lose the round.
- Once all players have finished making decisions, the dealer reveals their hidden card and continues drawing cards until their hand value reaches 17 or higher.
- If the dealer's hand value exceeds 21, they bust, and all players who haven't busted win the round.
- If both a player and the dealer have hands with values less than or equal to 21, the hand with the higher value wins. If the values are the same, it's a push (tie).

Please note that this implementation of Blackjack does not include features such as splitting, doubling down, or insurance.
