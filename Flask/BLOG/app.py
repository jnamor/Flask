from flask import Flask, request, render_template
from importlib_metadata import entry_points
import datetime

app = Flask (__name__)
entries = []

@app.route("/home", methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content")
        entries.append(entry_content)
        # entries.append({"content": entry_content,
        #         "date": datetime.datetime.today().strftime("%b %d")})
    
    return render_template('home.html', entries=entries)

if __name__ == '__main__':
   app.run(debug = True)