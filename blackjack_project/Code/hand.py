import numpy as np

cards_dict = {
	"A": 1,
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"T": 10,
	"J": 10,
	"Q": 10,
	"K": 10,
}
cards = list(cards_dict.keys())
numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10]

class Hand(list):
	# initializes hand with two cards
	def __init__(self):
		self.total = 0
		self.soft_total = 0
		self.draw_card()
		self.draw_card()
		self.bust = False

	# displays cards delimited with a space
	def  __str__(self):
		card_string = ""
		for card in self:
			card_string += str(card) + " "
		return card_string

	# picks a card from the deck
	def get_card(self):
		card = np.random.choice(cards)
		return card

	# adds another card to the hand
	def draw_card(self):
		card = self.get_card()
		value = cards_dict[card]
		self.total += value
		if card == "A" and self.soft_total < 11:
			self.soft_total += 11
		else:
			self.soft_total += value
		if self.soft_total > 21:
				self.soft_total = self.total
		self.append(card)
	

	def hit(self):
		self.draw_card()
		self.bust = self.total > 21
		print(self)
		self.display_total()
	
	def display_total(self):
		print("Total: " + str(self.total))
		if self.soft_total != self.total and self.soft_total <= 21:
			print("Soft total: " + str(self.soft_total))
	
	def display_your_cards(self, prefix):
		print(prefix + str(self))

	def display_dealer_cards(self):
		print ("Dealer's cards: * " + str(self[1]))
	
	def check_for_blackjack(self):
		return len(self) == 2 and self.soft_total == 21