# # from flask import Flask, render_template

# # app = Flask(__name__)


# # @app.route("/")
# # def home():
# #     message = "Hello from Python!"
# #     return render_template("index.html", message=message)


# # if __name__ == "__main__":
# #     app.run(debug=True)

# import json
# import pandas as pd
# from flask import Flask, render_template, request

# app = Flask(__name__)

# CSV_PATH = r"E:\FCAI\Dataset Experiment\data\raw\credit_g.csv"
# df = pd.read_csv(CSV_PATH)


# @app.route("/")
# def home():
#     limit = request.args.get("limit", "1")

#     if limit == "ALL":
#         json_str = df[df["class"] == "good"].to_json(orient="records", indent=2)
#     else:
#         try:
#             num = int(limit)
#             json_str = (
#                 df[df["class"] == "good"].head(num).to_json(orient="records", indent=2)
#             )
#         except ValueError:
#             json_str = (
#                 df[df["class"] == "good"].head(1).to_json(orient="records", indent=2)
#             )

#     records = json.loads(json_str)

#     return render_template("index.html", records=records, selected=limit)


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    if request.method == "POST":
        query = request.form.get("query")
        if query=="Python Programming":
            try:
                # Fetch top 5 Google results
                results = list(search(query, num_results=5, lang="en", region="us"))
            except Exception as e:
                results = [f"Error: {e}"]

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
