from flask import Flask
import random

# python -m flask --app hello run
# https://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf
# https://github.com/appbrewery/terminal-mac-cheatsheet
"""
app = Flask(__name__)

 what is __name__?
Because we're creating this app from this Flask class and in order to initialize a new Flask application,
there is only one required input, and that is the import_name.
if we print this __name__, it prints out __main__. 

< https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes >
The name is one of the special attribute that's built into Python
At any given point, you could tap into the name to find out what is the current class, function,
method, or descriptor's name.

< https://docs.python.org/3/library/__main__.html >
When we get __main__, what it's telling us is basically we're executing the code in a particular module. 
So that means it's run as a script or from an interactive prompt, but it's not run from an imported module.

It gives us this code here.

> 
    if the __name__ == "__main__":
    # then execute something only if it's run as a script. 
    # Execute when the module is not initialized from an import statement. 
<
-----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run()

one of the common ways that you'll see people run Flask apps.
You'll see if __name__ is double equal to __main__ as a string,
so exactly what was printed just now when we printed out this name,
well, if this is the case, then that means we're running the code from within this current file.
We're running hello.py. 

So in that case, we're going to tap into our app and we're going to call the run method.
Now this > app.run() < basically does exactly the same thing as when we went into the terminal and
we said flask run. 

But notice when we say flask run:
firstly, we have to provide the FLASK_APP environment variable
secondly, we have to stop the code using control + c instead of using our normal run and stop.

But if we use app.run, we can now use our standard controls.
So I can simply hit run to run this hello.py, and it will start serving up our Flask app 
at this address just as it did before, when we did flask run. And instead of using control + c to quit,
we can simply use the stop to stop our Flask application, making it a lot easier.

Basically by providing the name to Flask, Flask will check that this is the current file 
where the app code is located. And we're not in fact using an imported module.

For example:
if you were to import the random module and print the random.__name__,
it printed the name of that module.
But the name that's printed from hello.py, which is the file that's being run is simply __main__.

So this basically denotes the file that is currently being run and you say, Run 'hello' Well then inside hello
name is going to be equal to main.
-----------------------------------------------------------------------------------------------------------------------
@app.route("/")


"""
app = Flask(__name__)
print(random.__name__)
print(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()

