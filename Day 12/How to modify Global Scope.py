#Modifying Global Scope
enemies = 1

def increase_enemies():
    #have to explicitly say that we have a global variable
    global enemies  
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies inside function: {enemies}")

"""
 You probably don't actually want to do this very often, because it's confusing and
 it's prone to creating bugs and errors. Because this variable with global scope
 could have been created anywhere in your code, right?
"""

"""
What if you wanted to have this functionality like a function that changes the number of enemies?
How can you achieve this without modifying the global scope within the function? 
 
you could use return statements instead, you actually just simply returned it as the output.
So return the current value of enemies + 1.Now once you call this function,
you'll get hold of the output and you can save it to the global variable enemies.
"""
enemiess = 1
def increase_enemies():
    print(f"Enemiess inside function: {enemiess}")
    return enemiess + 1

enemiess = increase_enemies()
print(f"Enemiess inside function: {enemiess}")