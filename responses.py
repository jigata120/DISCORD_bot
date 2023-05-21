class Games:
    
   # Define a function to handle the "poker" command
    def poker(self):
            gm = Games()
            #suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            hand = random.sample([f"{card} of {suit}" for card in ranks for suit in suits], 5)
            hand_str = "\n".join(hand)
            combination = gm.check_hand(hand)
            if combination == '😥High card!😥':#' 💥💥💥Two pairs!💥💥💥'
                return f"🍀𝑱𝑼𝑺𝑻 𝑩𝑬𝑳𝑰𝑽𝑬🍀\n🃏Here are your 5 random cards🃏:\n{hand_str}\n{combination}"
            else:
                return f"🍀𝑨𝑹𝑬 𝑼 𝑳𝑼𝑪𝑲𝒀🍀\nHere are your 5 random cards:\n{hand_str}\n{combination}!"
 
    # Define a function to check for poker combinations in a hand of cards
    def check_hand(self,hand):
        values = [card.split()[0] for card in hand]
        suits = [card.split()[2] for card in hand]
        values.sort(key=lambda x: ranks.index(x))
        if len(set(suits)) == 1:
            if values ==  ['🅰', "10", "Jack", "Queen", "👑"]:
                return '💥💥💥💥💥💥Royal flush!💥💥💥💥💥💥'
            if ''.join(values) in '23456789TJQKA':
                return '💥💥💥💥💥Straight flush!💥💥💥💥💥'
            if all(values.count(value) == 1 for value in values):
                return 'Flush!'
        if ''.join(values) in '23456789TJQKA':
            return '💥💥💥💥Straight!💥💥💥💥'
        if any(values.count(value) == 4 for value in values):
            return '💥💥💥💥Four of a kind!💥💥💥💥'
        if set(values) == set(hand):
            return '💥💥💥Three of a kind!💥💥💥'
        pairs = [value for value in values if values.count(value) == 2]
        if len(pairs) == 2:
            return '💥Pair!💥'
        if len(pairs) == 1:
            return' 💥💥Two pairs!💥💥'
        return '😥High card!😥'


roll = Moves()
gm = Games()
def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey [message]!'
    if p_message == 'admin':
        customoutput = str(input('customoutput'))
        return customoutput
    if p_message[0:1]=='!':
        return f'{p_message[1:10]} e [smth] 😂'
    if p_message == 'roll':
        
        return '🎲='+str(roll.dice())

    if p_message == 'help':
        return "`COMMANDS:\nhello|roll = 🎲|!help = commands\n!+ANY (name) = Поздрав \n С команда ('poker')-можеш да опиташ късмета си.`"
    if p_message =='poker':
         return gm.poker()#gm.game_
    #  return 'Yeah, I don\'t know. Try typing "!help".'  

