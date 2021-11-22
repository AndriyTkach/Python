from flask import Flask
from time import strftime
from datetime import datetime, timedelta
app = Flask(__name__)

# <timezone>  format - UTC+2, UTC+0 ...
@app.route('/<timezone>')
def show_time(timezone):
    utc = datetime.utcnow()
    time = utc + timedelta(hours=int(timezone[4:]))
    return '<h1> Время: ' + time.strftime("%H:%M:%S") + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)
