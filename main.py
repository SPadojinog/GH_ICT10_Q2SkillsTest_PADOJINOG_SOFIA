from pyscript import display, document

# Individual club dictionaries
communication_arts = {
    "Name": "✍️ Communication Arts Club",
    "Description": "Improve writing, speaking, and multimedia skills.",
    "Meeting": "Wednesday 4:00–5:30 PM",
    "Location": "MMHALL",
    "Advisor": "Mr. Loreto",
    "Members": 20,
    "Category": "Arts",
}

science_club = {
    "Name": "♟️ Science Club",
    "Description": "Conduct experiments, explore scientific phenomena, and join science fairs.",
    "Meeting": "Thursday 3:30–4:00 PM",
    "Location": "Science Lab",
    "Advisor": "Mr. Calpo",
    "Members": 18,
    "Category": "STEM",
}

volleyball_varsity = {
    "Name": "🏅 Volleyball Varsity",
    "Description": "Train, practice, and compete in interschool volleyball tournaments.",
    "Meeting": "Tuesday 3:00–5:00 PM",
    "Location": "Quadrangle",
    "Advisor": "Coach Gervacio",
    "Members": 15,
    "Category": "Sports",
}

def show_CommunicationArts(e):
    document.getElementById('club-name').innerHTML = ""
    document.getElementById('club-description').innerHTML = ""
    document.getElementById('club-meeting').innerHTML = ""
    document.getElementById('club-location').innerHTML = ""
    document.getElementById('club-advisor').innerHTML = ""
    document.getElementById('club-members').innerHTML = ""
    document.getElementById('club-category').innerHTML = ""

    display(communication_arts["Name"], target="club-name")
    display(communication_arts["Description"], target="club-description")
    display(communication_arts["Meeting"], target="club-meeting")
    display(communication_arts["Location"], target="club-location")
    display(communication_arts["Advisor"], target="club-advisor")
    display(communication_arts["Members"], target="club-members")
    display(communication_arts["Category"], target="club-category")

def show_ScienceClub(e):
    document.getElementById('club-name').innerHTML = ""
    document.getElementById('club-description').innerHTML = ""
    document.getElementById('club-meeting').innerHTML = ""
    document.getElementById('club-location').innerHTML = ""
    document.getElementById('club-advisor').innerHTML = ""
    document.getElementById('club-members').innerHTML = ""
    document.getElementById('club-category').innerHTML = ""

    display(science_club["Name"], target="club-name")
    display(science_club["Description"], target="club-description")
    display(science_club["Meeting"], target="club-meeting")
    display(science_club["Location"], target="club-location")
    display(science_club["Advisor"], target="club-advisor")
    display(science_club["Members"], target="club-members")
    display(science_club["Category"], target="club-category")

def show_VolleyballVarsity(e):
    document.getElementById('club-name').innerHTML = ""
    document.getElementById('club-description').innerHTML = ""
    document.getElementById('club-meeting').innerHTML = ""
    document.getElementById('club-location').innerHTML = ""
    document.getElementById('club-advisor').innerHTML = ""
    document.getElementById('club-members').innerHTML = ""
    document.getElementById('club-category').innerHTML = ""

    display(volleyball_varsity["Name"], target="club-name")
    display(volleyball_varsity["Description"], target="club-description")
    display(volleyball_varsity["Meeting"], target="club-meeting")
    display(volleyball_varsity["Location"], target="club-location")
    display(volleyball_varsity["Advisor"], target="club-advisor")
    display(volleyball_varsity["Members"], target="club-members")
    display(volleyball_varsity["Category"], target="club-category")