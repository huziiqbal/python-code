from abc import ABC, abstractmethod
from random import randint, choice


# -------------------- BOARD TILES --------------------

class Tile:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def action(self, player, game):
        pass


class Property(Tile):
    def __init__(self, name, position, price, rent):
        super().__init__(name, position)
        self.price = price
        self.rent = rent
        self.owner = None
        self.level = 0

    def buy(self, player):
        if self.owner is None and player.money >= self.price:
            player.money -= self.price
            player.properties.append(self)
            self.owner = player
            return True
        return False

    def calculate_rent(self):
        return self.rent * (self.level + 1)

    def upgrade(self):
        self.level += 1

    def action(self, player, game):
        if self.owner is None:
            player.buy_decision(self)

        elif self.owner != player:
            amount = self.calculate_rent()
            player.pay(amount, self.owner)


class Chance(Tile):

    def __init__(self, position):
        super().__init__("Chance", position)

    def action(self, player, game):
        event = choice(game.events)
        event(player)


# -------------------- PLAYER --------------------

class Player(ABC):

    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.in_jail = False
        self.bankrupt = False

    def move(self, value, board_size):
        self.position = (self.position + value) % board_size

    def pay(self, amount, receiver=None):

        self.money -= amount

        if receiver:
            receiver.money += amount

        if self.money < 0:
            self.bankrupt = True

    @abstractmethod
    def buy_decision(self, property):
        pass


class HumanPlayer(Player):

    def buy_decision(self, property):
        property.buy(self)


class AIPlayer(Player):

    def buy_decision(self, property):

        if property.price < self.money * 0.4:
            property.buy(self)


# -------------------- DICE --------------------

class Dice:

    def roll(self):
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        return d1, d2


# -------------------- BANK --------------------

class Bank:

    def __init__(self):
        self.money = 1000000

    def reward(self, player, amount):
        player.money += amount
        self.money -= amount


# -------------------- GAME --------------------

class Game:

    def __init__(self):

        self.bank = Bank()
        self.dice = Dice()

        self.players = [
            HumanPlayer("Huzaifa"),
            AIPlayer("Computer")
        ]

        self.events = [
            lambda p: setattr(p, "money", p.money + 200),
            lambda p: setattr(p, "money", p.money - 150),
            lambda p: setattr(p, "position", 0),
            lambda p: setattr(p, "in_jail", True)
        ]

        self.board = self.create_board()

        self.turn = 0
        self.round = 1

    def create_board(self):

        board = []

        for i in range(20):

            if i % 5 == 0:
                board.append(Chance(i))

            else:
                board.append(
                    Property(
                        f"Property {i}",
                        i,
                        price=100 + i * 20,
                        rent=20 + i * 5
                    )
                )

        return board

    def current_player(self):
        return self.players[self.turn]

    def next_turn(self):

        self.turn += 1

        if self.turn >= len(self.players):
            self.turn = 0
            self.round += 1

    def remove_bankrupt(self):

        alive = []

        for p in self.players:

            if not p.bankrupt:
                alive.append(p)

            else:

                for prop in p.properties:
                    prop.owner = None

        self.players = alive

    def take_turn(self):

        player = self.current_player()

        if player.in_jail:
            player.in_jail = False
            self.next_turn()
            return

        d1, d2 = self.dice.roll()

        total = d1 + d2

        old = player.position

        player.move(total, len(self.board))

        if player.position < old:
            self.bank.reward(player, 200)

        tile = self.board[player.position]

        tile.action(player, self)

        self.remove_bankrupt()

        if len(self.players) > 1:
            self.next_turn()

    def leaderboard(self):

        return sorted(
            self.players,
            key=lambda p: (
                p.money +
                sum(x.price for x in p.properties)
            ),
            reverse=True
        )

    def print_status(self):

        print("-" * 40)

        for p in self.players:

            print(
                f"{p.name:10}"
                f" Money:{p.money:5}"
                f" Position:{p.position:2}"
                f" Properties:{len(p.properties)}"
            )

        print("-" * 40)

    def play(self):

        while len(self.players )> 1 and self.round <= 100:

            self.take_turn()

            self.print_status()

        print("\nWinner:")

        print(self.leaderboard()[0].name)

if __name__ == "__main":

    game = Game()

    game.play()

