# Code from - https://www.digitalocean.com/community/tutorials/bleu-score-in-python

from nltk.translate.bleu_score import sentence_bleu

# In the inputfile.txt, each new line is a new set of original lyrics (from the testing dataset)

with open('/Users/mehulaneja/NLP Workspace/FinalProject/BLEU/inputf.txt') as inputf:
    lines = inputf.readlines()

i = 0
for line in lines:
    lines[i] = line.split()
    i += 1
    

# Candidate is our machine generated lyrics
candidate = "I was singing, I was singin' 'round the world Singing from a field of my mind There's no one to tell me what you've been waiting for So many reasons Why we're still here in your head? (Ah-ah) You don't even know how it happened We were all just kids with our heads on cresciences The only thing that matters is love".split()

#print('Individual 1-gram: %f' % sentence_bleu(lines, candidate, weights=(1, 0, 0, 0)))
#print('Individual 2-gram: %f' % sentence_bleu(lines, candidate, weights=(0, 1, 0, 0)))
#print('Individual 3-gram: %f' % sentence_bleu(lines, candidate, weights=(0, 0, 1, 0)))
#print('Individual 4-gram: %f' % sentence_bleu(lines, candidate, weights=(0, 0, 0, 1)))
print('Original BLEU score: %f' % sentence_bleu(lines, candidate, weights=(0.25, 0.25, 0.25, 0.25))) # cumulative 4-gram BLEU score










