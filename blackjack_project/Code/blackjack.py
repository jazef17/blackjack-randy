#blackjack bot

import numpy as np
import time
from hand import Hand

# plays for the dealer
# dealer will hit until cards total 17 or more
def play_for_dealer(dealer_cards):
	dealer_cards.display_your_cards("Dealer cards: ")
	time.sleep(1)
	while dealer_cards.total < 17 and dealer_cards.soft_total < 18:
		print("Dealer hits.")
		dealer_cards.hit()
		time.sleep(1.5)
		if dealer_cards.total > 21:
			print("Dealer busts!")
			break
		dealer_cards.display_your_cards("Dealer cards: ")
	return dealer_cards

# determines winning logic
# + if player wins
# 0 if push
# - if push
def you_win(my_cards: Hand, dealer_cards: Hand):
	if my_cards.bust:
		return 0
	if my_cards.total < 21 and dealer_cards.bust:
		return 1
	
	a = my_cards.total - dealer_cards.total
	b = my_cards.soft_total - dealer_cards.soft_total
	c = my_cards.total - dealer_cards.soft_total
	d = my_cards.soft_total - dealer_cards.total
	return min([a,b,c,d], key=lambda x: abs(x))

def play():
	my_cards = Hand()
	dealer_cards = Hand()
	dealer_cards.display_dealer_cards()
	my_cards.display_your_cards("Your cards: ")

	# Check for blackjack
	dealer_blackjack = dealer_cards.check_for_blackjack()
	if my_cards.check_for_blackjack():
		print("Blackjack!")
		time.sleep(1)
		if dealer_blackjack:
			print("Dealer also blackjacks.")
			time.sleep(1)
			print("Push!")
		print("You win!")
		return 1
	if dealer_blackjack:
		print("Dealer blackjacks!")
		time.sleep(1)
		print("You lose...")
		return -1

	response = input()
	while (response != "stop") and (response != "stay") and not my_cards.bust:
		if response == "hit":
			time.sleep(1)
			my_cards.hit()
			if my_cards.bust:
				print("Bust!")
				break
		response = input()
	
	if response == "stop":
		return 0

	if my_cards.bust:
		print("You lose...")
		return -1

	dealer_cards = play_for_dealer(dealer_cards)
	result = you_win(my_cards, dealer_cards)

	if result > 0:
		print("You win!")
	elif result == 0:
		print("Push!")
	else:
		print("You lose...")
	return result

def get_bet(chips: int):
	bet = None
	while bet is None:
		try:
			bet = int(input("Enter the amount you'd like to bet: "))
			if bet <= 0 or bet > chips:
				print(f"Bet must be an integer between 1 and {chips}")
				bet = None
		except ValueError:
			print(f"Bet must be an integer between 1 and {chips}")
	return bet

def payout_chips(chips, bet, result):
	return chips + (np.sign(result) * bet)

def loan():
	print("Uh oh! You ran out of chips!")
	answer = input("Would you like to take out a loan?")
	if answer == "yes":
		return 100
	return 0

def main():
	chips = 100
	print("Welcome to Blackjack!")
	print("Chip total: " + str(chips))
	playing = input("Would you like to play?")
	while playing == "yes":
		bet = get_bet(chips)
		result = play()
		chips = payout_chips(chips, bet, result)
		print("Chip total: " + str(chips))
		time.sleep(0.5)
		if chips <= 0:
			chips += loan()
			if chips <= 0:
				break
		print("Chip total: " + str(chips))
		playing = input("Play again?")
	return

if __name__ == '__main__':
    main()

# TODO:
