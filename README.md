# haiku-bot

## What is this?

haiku-bot is a pretty simple script attemping to automatically generate original haikus using *restricted Markov chains*.

That sounds fancy, but basically all it means is given n number of words (i.e. "I want"), what is the most likely word to come next in a given text.

In order to try and make a haiku, rather that just text, we need to impose some restrictions, mainly syllable based, so rather than **what's the next most likely word**, instead we can ask **what's the next most likely word with the number of syllables needed to make this a haiku**.

Depending on the dataset used for training, this restriction might not be possible, in which case we just pick the most likely word and disregard syllable. This means not all outputs will be true haikus. Syllables are also detected from a good regex guess based on vowels, so these will sometimes be wrong too ('slayed' would be read as a two syllable word for instance).

That's pretty much it. There's a slight extra thrown in to try to encourage original text (rather than just repeats of sentences already in the training data) which is that rather than picking the next most likely, we actually randomly select any word that follows in the training data, but *weight the selection towards the most likely ones*.

## How to run

You can run as-is by downloading the github and just running the 'main' file (there's a few requirements around modules, and nltk in particular involves downloading some specifics).

It'll automatically use any text inside the 'text' folder as training data, so chopping and changing this will affect the output. There's a bunch of copyright free examples already there.

The code itself is pretty sure though. "haiku_bot.py" is less than 100 lines of code- so feel free to pick apart and change anything.

## Some examples of outputs (grammar added)

In these examples, punctuation has been added in (any output haikus will be lower case and without punctuation)


**Trained from Onoto Watanna's A Japanese Blossom:**
> There were only two /
> clerks left in your house - pluck out /
> one branch, one flower.

**Trained from J.K Rowling's Harry Potter:**
> Met a dragon trying /
> to find out how to get past /
> Fluffy, and he could.

**Trained from T.S. Eliot's The Waste Land:**
> Warm covering earth /
> in forgetful snow feeding /
> a little patience here.

**Trained from Walt Whitman's Leaves of Grass:**
> In myself I could /
> look with the old: the eighty /
> third year of meteors.

**Trained from Agatha Christie's The Secret Adversary:**
> Of it: it's a toss /
> up, but I can t help it if /
> you want to know how.


**Trained from Emanuel Kant's The Critique of Pure Reason:**
> a logical place /
> upon this point of time and /
> thus, the conception.

**Trained from collection of texts:**
> Disturbed if the /
> rough wave foameth and angrily /
> resisteth its keel.

> Mishmash. That is the /
> world itself and the way from /
> fame must be but it.

> Of the world: is the /
> world weary of the highest / 
> hope - To soar away?
