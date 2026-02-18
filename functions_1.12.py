import secrets
import string
import time

TARGET_STRING = list("methinks it is like a weasel")
TARGET_LENGTH = len(TARGET_STRING)

def generate_string():
	random_choice = string.ascii_lowercase + " "
	return [secrets.choice(random_choice) for _ in range(TARGET_LENGTH)]


def generate_score():
	guess = generate_string()
	# print(f"Guess: {''.join(guess)}   Target: {''.join(TARGET_STRING)}")
	score = 0
	for i in range(TARGET_LENGTH):
		if TARGET_STRING[i] == guess[i]:
			score += 1
	return (score, ''.join(guess))


def generate_result():
	tries = 1
	best_score = 0
	best_guess = ''
	best_accuracy = 0
	score, guess = generate_score()
	while True:
		print(f'Trying {tries} time...')
		# print(f'Best score: {score}, Best guess: {guess}')
		accuracy_percent = (score / TARGET_LENGTH) * 100
		if accuracy_percent >= 100:
			return f"Wohoo! Finally got the perfect guess: {guess}"
		elif score > best_score:
			best_guess = guess
			best_score = score
			best_accuracy = accuracy_percent
		if tries % 1000 == 0:
			print(f"Best guess so far: '{best_guess}'\n  Score: {best_score}  Accuracy: {best_accuracy:.2f}")
			time.sleep(5) 
		tries += 1


def generate_result_enhanced():
	guess_domain = string.ascii_lowercase + " "
	tries = 1
	score = 0
	index = 0
	guess = generate_string()
	while index < TARGET_LENGTH:
		print(f'Trying {tries} time...Modifying index {index}  Guess: {''.join(guess)}  Target: {''.join(TARGET_STRING)}')
		if guess[index] == TARGET_STRING[index]:
			if index + 1 == TARGET_LENGTH:
				return f"Found Target string: {''.join(TARGET_STRING)} with a guess {''.join(guess)} in {tries} tries"
			score += 1
			index += 1
		else:
			guess[index] = secrets.choice(guess_domain)
		if tries % 20 == 0:
			print(f"Score so far: {score}\nGuess so far: {guess}\nAccuracy so far: {score / TARGET_LENGTH * 100}")
			# time.sleep(8)
		tries += 1
print(generate_result_enhanced())


