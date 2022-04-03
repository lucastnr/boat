from time import sleep

class Automato():
  # 0 = ESQUERDA
  # 1 = DIREITA
  estados = {
    "fazendeiro": 0,
    "couve": 0,
    "cabra": 0,
    "lobo": 0
  }


  def __init__(self):
   self.loop()

  def loop(self):
    fazendeiro = self.estados["fazendeiro"]
    couve = self.estados["couve"]
    cabra = self.estados["cabra"]
    lobo = self.estados["lobo"]

    print(self.estados)

    # Todos na esqueda
    if fazendeiro == 0 and couve == 0 and cabra == 0 and lobo == 0:
      self.travessia({ 
      "fazendeiro": 1,
      "couve": 0,
      "cabra": 1,
      "lobo": 0
      })
    elif fazendeiro == 1 and couve == 0 and cabra == 1 and lobo == 0:
      self.travessia({ 
      "fazendeiro": 0,
      "couve": 0,
      "cabra": 1,
      "lobo": 0
      })
    elif fazendeiro == 0 and couve == 0 and cabra == 1 and lobo == 0:
      self.travessia({ 
      "fazendeiro": 1,
      "couve": 0,
      "cabra": 1,
      "lobo": 1
      })
    elif fazendeiro == 1 and couve == 0 and cabra == 1 and lobo == 1:
      self.travessia({ 
      "fazendeiro": 0,
      "couve": 0,
      "cabra": 0,
      "lobo": 1
      })
    elif fazendeiro == 0 and couve == 0 and cabra == 0 and lobo == 1:
      self.travessia({ 
      "fazendeiro": 1,
      "couve": 1,
      "cabra": 0,
      "lobo": 1
      })
    elif fazendeiro == 1 and couve == 1 and cabra == 0 and lobo == 1:
      self.travessia({ 
      "fazendeiro": 0,
      "couve": 1,
      "cabra": 0,
      "lobo": 1
      })
    elif fazendeiro == 0 and couve == 1 and cabra == 0 and lobo == 1:
      self.travessia({ 
      "fazendeiro": 1,
      "couve": 1,
      "cabra": 1,
      "lobo": 1
      })

    if fazendeiro == 1 and couve == 1 and cabra == 0 and lobo == 1:
      return

  def travessia(self, estados):
    self.estados["fazendeiro"] = estados["fazendeiro"]
    self.estados["couve"] = estados["couve"]
    self.estados["cabra"] = estados["cabra"]
    self.estados["lobo"] = estados["lobo"]