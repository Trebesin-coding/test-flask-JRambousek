from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# with open("data/recenze.json", "r") as f:
#     recenze_json = json.load(f)


@app.route("/")
def vitej():
    return render_template("vitej.html")

@app.route("/form")
def form():
    name = request.args.get("name", default="______")
    recenze = request.args.get("recenze", default="______")
    print(name, recenze)
    if name and recenze:
        if recenze == "nic":
            return render_template("skoro.html")
        elif len(recenze) <= 3:
            return render_template("skoro.html")

    # napsana_recenze = {
    #     "jmeno": name,
    #     "recenze": recenze
    # }
    # recenze_json.append(napsana_recenze)

    # with open("data/renceze.json", "w") as f:
    #     json.dump(recenze_json, f)
    return render_template("form.html", name=name, renceze=recenze)

if __name__ == "__main__":
    app.run(debug=True)