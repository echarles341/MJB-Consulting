# import website package created from __init__
# create the application and run it
from website import create_app

app = create_app()
# only if the following file then create the app
# start a web server
# will run the new code every time changes are made in the python code
# Note: remember to turn off code when in production
if __name__ == '__main__':
    app.run(debug=True, port=8000)
