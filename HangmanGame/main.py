import words
import random
import art

print(art.logo)
random_word = random.choice(words.word_list)
#print(random_word)
word_len = len(random_word)

blanks = []
for i in range(0, word_len):
  blanks +="_"
lives = len(random_word)
while "_" in blanks:  
  guess = input("GUESS A LETTER: ").lower()
  
  for i in range(0, word_len):
    if random_word[i] == guess:
      blanks[i]=guess

  if guess not in random_word:
    lives -= 1
    if lives==0:
      print("YOU LOSE😞 ")
      print("THE WORD WAS: "+random_word)
      break
      
  print(f"{' '.join(blanks)}")  
  print(f"CHANCES LEFT:{lives}")
  print(art.stages[lives])
  if "_" not in blanks:
    print("YOU WON🥳")
    break