from flask import Flask
app = Flask(__name__)
print("initiated the app! With a name of:", __name__)

@app.route('/')
def homepage():
    print("Hey I'm visiting the homepage!")
    return "Hello world!"

if __name__ == '__main__':
    print("App is starting...I think?")
    app.run(use_reloader=True)
    print("Umm...no idea what/how this message will be seen...")
