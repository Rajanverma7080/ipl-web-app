from flask import Flask,render_template,request

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/teams')
@app.route("/teams")
def teams():

    teams = [
        {
            "name": "Chennai Super Kings",
            "short_name": "CSK",
            "logo": "CSK_logo.png"
        },
        {
            "name": "Mumbai Indians",
            "short_name": "MI",
            "logo": "MI_logo.png"
        },
        {
            "name": "Royal Challengers Bangalore",
            "short_name": "RCB",
            "logo": "RCB_logo.png"
        },
        {
            "name": "Kolkata Knight Riders",
            "short_name": "KKR",
            "logo": "KKR_logo.png"
        },
        {
            "name": "Rajasthan Royals",
            "short_name": "RR",
            "logo": "RR_logo.png"
        },
        {
            "name": "Rajasthan Royals",
            "short_name": "RR",
            "logo": "DC_logo.png"
        },
        {
            "name": "Rajasthan Royals",
            "short_name": "RR",
            "logo": "LSG_logo.png"
        },
        {
            "name": "Rajasthan Royals",
            "short_name": "RR",
            "logo": "PBKS_logo.png"
        },
        {
            "name": "Rajasthan Royals",
            "short_name": "RR",
            "logo": "SRH_logo.png"
        },
        {
            "name": "Rajasthan Royals",
            "short_name": "RR",
            "logo": "GT_logo.png"
        },
    ]

    return render_template(
        "teams.html",
        teams=teams
    )

if __name__ == '__main__':
    app.run(debug=True ,port=7000)