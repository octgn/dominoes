def rotateClockwise(card, x = 0, y = 0):
  mute()
  if card.orientation == Rot270:
    card.orientation = Rot0
  else:
    card.orientation += Rot90

def rotateCounter(card, x = 0, y = 0):
  mute()
  if card.orientation == Rot0:
    card.orientation = Rot270
  else:
    card.orientation -= Rot90

def moveup(card, x = 0, y = 0):
  mute()
  (x,y) = card.position
  card.moveToTable(x,y-1)

def movedown(card, x = 0, y = 0):
  mute()
  (x,y) = card.position
  card.moveToTable(x,y+1)

def moveleft(card, x = 0, y = 0):
  mute()
  (x,y) = card.position
  card.moveToTable(x-1,y)

def moveright(card, x = 0, y = 0):
  mute()
  (x,y) = card.position
  card.moveToTable(x+1,y)

def draw(group, x = 0, y = 0, randompos = 0, decksize = 0):
  mute()
  deck = getGlobalVariable("Deck")##Retrieves a copy of the shared Draw Pile global variable
  if deck == "CHECKOUT":##Prevents card drawing if the Draw Pile is locked
    whisper("Deck is currently in use, please try this function again.")
    return
  deck = eval(deck)##Converts the Draw Pile into a true list, as global variables must be stored as strings
  if len(deck) == 0:##Prevents card drawing if the Draw Pile is empty
    whisper("No dominoes left in Draw Pile!")
    return
  setGlobalVariable("Deck", "CHECKOUT")##Locks the Draw Pile to prevent other players from changing it while this function processes
  decksize = len(deck) - 1##counts the number of dominoes in the Pile, then subtracts by one to obtain the upper boundary of the list index
  randompos = rnd(0, decksize)##Generate a random number corresponding to an index in the Draw Pile list
  domino = deck[randompos]##Identifies the specific domino at that position of the list
  card = table.create(domino,0,0,1,persist=True)##Creates the randomly selected domino
  card.moveTo(me.hand)
  del deck[randompos]##Removes the domino from the Draw Pile so others won't draw it again
  setGlobalVariable("Deck", str(deck))##Stores the new Draw Pile into the shared global variable
  notify("{} drew a domino from the Draw Pile.".format(me))
  
def doublesix(group, x = 0, y = 0, randompos = 0, decksize = 0, loop = 0):
  mute()
  if getGlobalVariable("Deck") == "CHECKOUT":##Prevents the function if the Draw Pile is locked
    whisper("Deck is currently in use, please try this function again.")
    return
  tablecount = sum(1 for card in table)
  handcount = sum(1 for card in me.hand)
  discardcount = sum(1 for card in shared.piles["Discard Pile"])
  if tablecount + handcount + discardcount != 0:##Cancels the function if there are dominoes in play, since the game hasn't been restarted
    whisper("There are currently dominoes in play, please Restart Game first.")
    return
  count = askInteger("Start the game with how many dominoes?", 7)
  if count == None: return##If the player cancels out of the box, its assumed they don't want to continue the function
  if len(players)*count > 28:##Makes sure there's enough dominoes to deal out to all players
    whisper("There aren't enough dominoes available to deal to each player! Try again with a different amount.")
    return
  setGlobalVariable("Deck", "CHECKOUT")##Locks the Draw Pile from manipulation
  tempdeck = list(doubleSixDeck)##Grabs the full ordered list of GUIDs of all cards in a Double Six game
  deck = [ ]
  notify("{} is starting a new Double-Six game, shuffling dominoes...".format(me))
  while len(tempdeck) > 0:##This is a shuffle algorithm to shuffle the list in tempdeck and store it in deck
    listsize = len(tempdeck) - 1
    pos = rnd(0, listsize)
    deck.append(tempdeck.pop(pos))
  notify("{} is dealing {} dominoes out.".format(me, count))
  while loop < count:##Each while loop deals one domino to each player, and loops for count times.  Functionally similar to card drawing
    for player in players:
      decksize = len(deck) - 1
      randompos = rnd(0, decksize)
      domino = deck[randompos]
      card = table.create(domino,0,0,1,persist=True)
      card.moveTo(player.hand)
      del deck[randompos]
    loop += 1##increments the loop count once one card has been dealt to each player
  setGlobalVariable("Deck", str(deck))##stores the Draw Pile into the global variable
  notify("{} started a new Double-Six game.".format(me))

def doublenine(group, x = 0, y = 0, randompos = 0, decksize = 0, loop = 0):
  mute()
  tablecount = sum(1 for card in table)
  handcount = sum(1 for card in me.hand)
  discardcount = sum(1 for card in shared.piles["Discard Pile"])
  if tablecount + handcount + discardcount != 0:
    whisper("There are currently dominoes in play, please Restart Game first.")
    return
  count = askInteger("Start the game with how many dominoes?", 7)
  if count == None: count = 0
  if len(players)*count > 55:
    whisper("There aren't enough dominoes available to deal to each player! Try again with a different amount.")
    return
  setGlobalVariable("Deck", "CHECKOUT")
  tempdeck = list(doubleNineDeck)
  deck = [ ]
  notify("{} is starting a new Double-Nine game, shuffling dominoes...".format(me))
  while len(tempdeck) > 0:
    listsize = len(tempdeck) - 1
    pos = rnd(0, listsize)
    deck.append(tempdeck.pop(pos))
  notify("{} is dealing {} dominoes out.".format(me, count))
  while loop < count:
    for player in players:
      decksize = len(deck) - 1
      randompos = rnd(0, decksize)
      domino = deck[randompos]
      card = table.create(domino,0,0,1,persist=True)
      card.moveTo(player.hand)
      del deck[randompos]
    loop += 1
  setGlobalVariable("Deck", str(deck))
  notify("{} started a new Double-Nine game.".format(me))

def discard(card, x = 0, y = 0):
  mute()
  src = card.group.name
  if src == Table:
    text = "the table"
  else:
    text = "their hand"
  card.isFaceUp = True
  notify("1")
  card.moveTo(shared.piles['Discard Pile'])
  notify("2")
  rnd(10,100)
  notify("{} discards {} from {}.".format(me, card, text))

def rolldie(group, x = 0, y = 0):
  mute()
  num = rnd(1,20)
  notify("{} rolls {} on a 20-sided die.".format(me, num))

doubleNineDeck = [
  "50d634aa-9aed-4583-81d6-c3097c090271",
  "92abea24-1caa-49ee-bfbf-f696d64b20d3",
  "9cf9663f-fff6-4b03-8519-01bd1ee1fc26",
  "b6746b63-4c1f-4f02-b3b3-2c3d5a1a2eae",
  "94f958d8-6348-473b-8db7-2d8223d30a3b",
  "c8de18c0-f455-41b1-bf6a-004e21ca8421",
  "9a1c3b7c-4f27-4d20-b447-9fc0064c843e",
  "54a2cd0d-506f-4f89-b9cc-db41cf93753a",
  "8720ca31-e1d0-4996-ba89-2a2a4ec9c5f4",
  "ad14face-d022-4e55-a5b0-0a47f9b470b9",
  "352df8b2-d24e-4013-8d77-db4bc2fa68b1",
  "8a239bdd-af69-4b6a-b51c-b9de988f7ffd",
  "fead3bb4-cc30-4907-a166-55fbed53d09f",
  "1cbd7a40-5338-4289-adc0-5e14ef3794bd",
  "a14b85f3-955b-43c4-8325-fde993736c81",
  "c6db9c8d-2403-4cb7-b062-8411d93f2548",
  "62c652e9-af51-4b92-b588-69b724bf9df7",
  "eceb9480-2fb5-4939-9f7f-667b8d716f2c",
  "29d750e6-e408-4c99-bfff-1f299fdeaf34",
  "67d2e2b6-d7fc-4ac5-a048-936247a97379",
  "4775fd74-6370-419e-8241-5f96c7141229",
  "20af19af-f6d3-42cf-8b91-9d8f5d3da606",
  "174aee05-188c-4d3c-b0ec-8d21eb095a1f",
  "1252ee8e-164e-4365-b1f2-8e851122ade3",
  "94f8e05d-d10e-493a-90a2-d873ce750254",
  "76219712-9ed5-4fe2-b6d1-b6d9b6e4ddd4",
  "0b5675e7-cbe7-416d-b96c-c2b4718e3fd4",
  "9704c2ae-f6c1-4fc0-8f11-b7b33fbd872e",
  "b39e81ee-5ec1-4bdc-a472-25978d20b55f",
  "8de3bebe-83a2-4a97-9506-c9b651e27d97",
  "aa6783d7-063e-4fee-821f-3d951be2bd67",
  "5723fe67-bb1a-4740-80bf-850891fb5d24",
  "1b4c4e1c-53aa-4bc5-8e31-dc615e435888",
  "daba07f3-5b9a-4397-b9d1-73264b6dd225",
  "c1727705-c27c-48bb-8a5a-8e7841f65a9c",
  "df7b1779-d11a-4858-baa8-bcd9e3cd5a32",
  "f4c6f4bf-4763-4603-816e-418603baddcc",
  "14367fcf-22f6-4419-841c-ed3368dbcbf0",
  "bb706db1-f32e-44dc-a3d9-83de2147c0f2",
  "ffde946c-fe4f-4805-a9ef-8c77068c9ea6",
  "83182bbb-1537-4d00-b12b-5fbd438a39e2",
  "bcfc99cb-3368-4084-a3bb-a664d689edcc",
  "1c31db16-6b53-4f94-9ec8-d71110b0f79e",
  "e05e1af7-7700-4d81-8b9e-64f6e41060a4",
  "6fc9fa89-82b8-4002-8fb0-46e5da48dfa9",
  "818823e0-8ea3-4b0a-b11f-6d5c4c26e4e0",
  "ba5af46e-bb00-443b-98e2-d13e10d1a069",
  "4124427c-2e0f-4e1f-aad6-20eb3ce90ed8",
  "2b40e12d-d3b7-43af-a710-c86ebb0d2740",
  "a0945f65-2ced-4376-bc0b-ee56320666ee",
  "cb5aa229-a7d1-42aa-b764-ce5a27fd7f82",
  "372cfdd0-6a72-4eeb-be5a-6c16a13c48b3",
  "c519ad62-b58d-4dd6-96d6-2d8944ca22c4",
  "9a43ba76-f6da-4b2e-afe7-77cb245955db",
  "5201e0a8-77fa-4411-8ef7-00ae5eda54a2"
]

doubleSixDeck = [
  "50d634aa-9aed-4583-81d6-c3097c090271",
  "92abea24-1caa-49ee-bfbf-f696d64b20d3",
  "9cf9663f-fff6-4b03-8519-01bd1ee1fc26",
  "b6746b63-4c1f-4f02-b3b3-2c3d5a1a2eae",
  "94f958d8-6348-473b-8db7-2d8223d30a3b",
  "c8de18c0-f455-41b1-bf6a-004e21ca8421",
  "9a1c3b7c-4f27-4d20-b447-9fc0064c843e",
  "352df8b2-d24e-4013-8d77-db4bc2fa68b1",
  "8a239bdd-af69-4b6a-b51c-b9de988f7ffd",
  "fead3bb4-cc30-4907-a166-55fbed53d09f",
  "1cbd7a40-5338-4289-adc0-5e14ef3794bd",
  "a14b85f3-955b-43c4-8325-fde993736c81",
  "c6db9c8d-2403-4cb7-b062-8411d93f2548",
  "67d2e2b6-d7fc-4ac5-a048-936247a97379",
  "4775fd74-6370-419e-8241-5f96c7141229",
  "20af19af-f6d3-42cf-8b91-9d8f5d3da606",
  "174aee05-188c-4d3c-b0ec-8d21eb095a1f",
  "1252ee8e-164e-4365-b1f2-8e851122ade3",
  "9704c2ae-f6c1-4fc0-8f11-b7b33fbd872e",
  "b39e81ee-5ec1-4bdc-a472-25978d20b55f",
  "8de3bebe-83a2-4a97-9506-c9b651e27d97",
  "aa6783d7-063e-4fee-821f-3d951be2bd67",
  "c1727705-c27c-48bb-8a5a-8e7841f65a9c",
  "df7b1779-d11a-4858-baa8-bcd9e3cd5a32",
  "f4c6f4bf-4763-4603-816e-418603baddcc",
  "83182bbb-1537-4d00-b12b-5fbd438a39e2",
  "bcfc99cb-3368-4084-a3bb-a664d689edcc",
  "818823e0-8ea3-4b0a-b11f-6d5c4c26e4e0"
]