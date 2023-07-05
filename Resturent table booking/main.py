
from Application import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    #modification can be seen by refreshing in page it self