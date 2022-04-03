class Automaton():
  # 0 = LEFT
  # 1 = RIGHT
  state = {
    "farmer": 0,
    "cabbage": 0,
    "goat": 0,
    "wolf": 0
  }


  def __init__(self):
   self.loop()

  def loop(self):
    farmer = self.state["farmer"]
    cabbage = self.state["cabbage"]
    goat = self.state["goat"]
    wolf = self.state["wolf"]

    print(self.state)

    # Todos na esqueda
    if farmer == 0 and cabbage == 0 and goat == 0 and wolf == 0:
      self.travessia({ 
      "farmer": 1,
      "cabbage": 0,
      "goat": 1,
      "wolf": 0
      })
    elif farmer == 1 and cabbage == 0 and goat == 1 and wolf == 0:
      self.travessia({ 
      "farmer": 0,
      "cabbage": 0,
      "goat": 1,
      "wolf": 0
      })
    elif farmer == 0 and cabbage == 0 and goat == 1 and wolf == 0:
      self.travessia({ 
      "farmer": 1,
      "cabbage": 0,
      "goat": 1,
      "wolf": 1
      })
    elif farmer == 1 and cabbage == 0 and goat == 1 and wolf == 1:
      self.travessia({ 
      "farmer": 0,
      "cabbage": 0,
      "goat": 0,
      "wolf": 1
      })
    elif farmer == 0 and cabbage == 0 and goat == 0 and wolf == 1:
      self.travessia({ 
      "farmer": 1,
      "cabbage": 1,
      "goat": 0,
      "wolf": 1
      })
    elif farmer == 1 and cabbage == 1 and goat == 0 and wolf == 1:
      self.travessia({ 
      "farmer": 0,
      "cabbage": 1,
      "goat": 0,
      "wolf": 1
      })
    elif farmer == 0 and cabbage == 1 and goat == 0 and wolf == 1:
      self.travessia({ 
      "farmer": 1,
      "cabbage": 1,
      "goat": 1,
      "wolf": 1
      })

    if farmer == 1 and cabbage == 1 and goat == 0 and wolf == 1:
      return

  def travessia(self, state):
    self.state["farmer"] = state["farmer"]
    self.state["cabbage"] = state["cabbage"]
    self.state["goat"] = state["goat"]
    self.state["wolf"] = state["wolf"]