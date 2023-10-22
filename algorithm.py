minute = 60
hour = 60 * minute
day = 24 * hour
week = 7 * day

fast_table = {
          0: [None, minute,  6 * minute, 10 * minute,     day, 4 * day],
     minute: [None, minute,  6 * minute, 10 * minute,     day, 4 * day],
 6 * minute: [None, minute,  6 * minute,     1 * day, 3 * day, 5 * day],
10 * minute: [None, minute, 10 * minute,   2.5 * day, 4 * day, 6 * day],
}

# ease means stars
def get_next_interval(ease, interval=None, repetition=None):
    # ease: this is going to be the rating that the user gives the card (1-5 stars depending on the ease, 1 being impossible and 5 being super easy)
    # repetition: each card is going to have a number to keep track of the repetition
    # interval: the interval (in seconds) between each population of the specific card
    difficulty = 6 - ease
    if repetition == None: repetition = 0
    if interval == None: interval = 60

    if interval in fast_table:
        return fast_table[interval][ease]
    
    if ease == 1: return 60
    if ease == 2: return max(interval + 35, 60)
    
    previous_interval_thing = previous_interval_calculator(interval, ease, repetition)
    ease_factor = easeFactor(difficulty, previous_interval_thing)
    
    if repetition <= 1: return round(ease_factor)
    else: return round(interval * ease_factor + 1)

# public static int create a method from the body, just name it and return the interval
# create a method that creates the array that sorts and stores the interval from smallest to largest and returns that
def easeFactor(ease, previousInterval):
    return previousInterval + (0.1 - (5 - ease) * (0.08 + (5 - ease) * 0.02))

difficulty_to_interval_first = [None, 43200, 3600, 900, 360, 60]
difficulty_to_interval_impossible = [None, 86400, 43200, 1800, 360, 60]
difficulty_to_interval_later = [None, 345600, 86400, 1800, 360, 60]

def previous_interval_calculator(interval, difficulty, repetition):
    if repetition < 1:
        return difficulty_to_interval_first[difficulty]
    elif repetition > 0 and repetition < 1:
        return difficulty_to_interval_impossible[difficulty]
    else:
        return difficulty_to_interval_later[difficulty]

# decks.objects.all
def pick_next(cards): # Returns a tuple (index, card)
    return min(enumerate(cards), key=lambda i_c : i_c[1].next_due)



