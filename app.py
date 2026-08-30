from flask import Flask,render_template,request,jsonify
import requests
import json

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



@app.route('/compare')
def team_fetch():
    response = requests.get('http://127.0.0.1:5000/api/teams')
    teams = response.json()['teams']
    return render_template('team_vs_team.html',teams = sorted(teams))


@app.route('/teamvteam')
def team_vs_team():

    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    # Default values
    result = None
    error = None

    # Get all teams
    response1 = requests.get(
        'http://127.0.0.1:5000/api/teams'
    )

    teams = response1.json()['teams']

    # Team information
    team_info = {
        "Chennai Super Kings": {
            "short": "CSK",
            "logo": "CSK_logo.png"
        },
        "Mumbai Indians": {
            "short": "MI",
            "logo": "MI_logo.png"
        },
        "Royal Challengers Bangalore": {
            "short": "RCB",
            "logo": "RCB_logo.png"
        },
        "Kolkata Knight Riders": {
            "short": "KKR",
            "logo": "KKR_logo.png"
        },
        "Rajasthan Royals": {
            "short": "RR",
            "logo": "RR_logo.png"
        },
        "Delhi Capitals": {
            "short": "DC",
            "logo": "DC_logo.png"
        },
        "Lucknow Super Giants": {
            "short": "LSG",
            "logo": "LSG_logo.png"
        },
        "Punjab Kings": {
            "short": "PBKS",
            "logo": "PBKS_logo.png"
        },
        "Sunrisers Hyderabad": {
            "short": "SRH",
            "logo": "SRH_logo.png"
        },
        "Gujarat Titans": {
            "short": "GT",
            "logo": "GT_logo.png"
        }
    }

    # If both teams are selected
    if team1 and team2:

        # Same team check
        if team1 == team2:

            error = "Please select two different teams."

        else:

            # Call your API
            response2 = requests.get(
                'http://127.0.0.1:5000/api/teamvteam',
                params={
                    'team1': team1,
                    'team2': team2
                }
            )

            if response2.status_code == 200:

                result = response2.json()

            else:

                error = "Unable to fetch team comparison."

    # Default values for template
    short1 = None
    short2 = None
    logo1 = None
    logo2 = None

    # Team 1 details
    if team1 in team_info:

        short1 = team_info[team1]["short"]
        logo1 = team_info[team1]["logo"]

    # Team 2 details
    if team2 in team_info:

        short2 = team_info[team2]["short"]
        logo2 = team_info[team2]["logo"]

    return render_template(
        'team_vs_team.html',
        teams=sorted(teams),
        result=result,
        error=error,
        team1=team1,
        team2=team2,
        short1=short1,
        short2=short2,
        logo1=logo1,
        logo2=logo2
    )

if __name__ == '__main__':
    app.run(debug=True ,port=7000)