################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  return enemies


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope 
"""Local scope exists within function.
Variable defined inside the functions can only be used inside the function.
Same goes to creating a new function inside a function"""
# Example
def drink_potion():
  potion_strength = 2
  print(potion_strength)
drink_potion()


#Global Scope
"""variable defined outside of a function can be
used inside and outside of a function"""
player_health = 10 

def drink_potion():
  potion_strength = 2
  print(player_health)

drink_potion()
print(player_health)

# Nested Function
"""
this drink_potion now has local scope within the function game.
So now in order to call this drink_potion, I have to be within the 
four walls of the game function.So whenever you give name to anything,
a function or a variable,you have to be aware of where you created it.
"""
def game():
  def drink_potions():
    potion_strengths = 2
    print(player_health)
  drink_potions()
  
drink_potions() # doesn't work


  


  
