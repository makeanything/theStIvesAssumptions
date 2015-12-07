##As I was going to St. Ives,
##I met a man with seven wives,
##Each wife had seven sacks,
##Each sack had seven cats,
##Each cat had seven kits:
##Kits, cats, sacks, and wives,
##How many were there going to St. Ives?

n = 1; # The "I" or narrator character and anyone I claim to be bringing with me.

m = 1; # man as the husband character

w = 7; # the man's seven wives

s = 7; # the number of sacks each wife is carrying

c = 7; # the number of cats in each sack

k = 7; # the number of kits each cat has

inOneSack = c + (c * (k*c));    #the contents of a sack, but not counting the sack.
includeSack = 1 + inOneSack;      #includes the sack itself as an entity

sacksCount = s * includeSack; #how much a single woman is carrying sacks times contents of sack.
sacksDontCount = s * inOneSack;


womenAreCarrying = w * sacksCount;

womenAndWhatTheyAreCarrying = w + womenAreCarrying;

includeHusbands = m + m * womenAndWhatTheyAreCarrying;

meToo = n + includeHusbands;

print womenAndWhatTheyAreCarrying; #see notes to understand why I'm skipping both includeHusbands & meToo. 

# Decision one : Do you want to count the sacks as entities here? Yes, but only because the question asks in part how many sacks are going to St. Ives.
# Position on possession of kits. Maternity/Paternity is no factor, each cat possesses seven kits. Nobody cares about maternity/paternity, each cat is simply in possession of seven kits.
# Answering the question specifically with the assumptions I am allowing. The question dissected does not include the husband. In fact, it doesn't ask to include the narrator.
#it specifically says encompassed in "Kits, cats, sacks, and wives" better yet call that scope "How many were there going to St. Ives?"
# 9 people were there, 49 sacks (known to contain felines) were there, 17,150 felines were there. So add the assumption that there were no other sacks there going to St. Ives.
# As just math this equals 7 * (7 * (7 + (7 * (7 * 7))
