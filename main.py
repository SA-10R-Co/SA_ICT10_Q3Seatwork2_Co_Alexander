from pyscript import document

def intrams_checker(e):
    out = document.getElementById("output")
    img_box = document.getElementById("image")

    out.innerHTML = ""
    img_box.innerHTML = ""

    reg = document.querySelector('input[name="registration"]:checked')
    clr = document.querySelector('input[name="clearance"]:checked')

    if not reg or not clr:
        out.innerHTML = "⚠ COMPLETE ALL REQUIREMENTS"
        return

    grade = int(document.getElementById("level").value)
    section = document.getElementById("section").value.lower()

    if reg.value != "registered":
        out.innerHTML = "❌ REGISTRATION REQUIRED"
        return

    if clr.value != "cleared":
        out.innerHTML = "❌ MEDICAL CLEARANCE REQUIRED"
        return

    if grade < 7 or grade > 10:
        out.innerHTML = "❌ INVALID GRADE LEVEL"
        return

    if section == "emerald":
        team, img = "BLUE BEARS", "blue bears.jpg"
    elif section == "ruby":
        team, img = "RED BULLDOGS", "red bulldogs.jpg"
    elif section == "sapphire":
        team, img = "YELLOW TIGERS", "yellow tigers.jpg"
    elif section == "topaz":
        team, img = "GREEN HORNETS", "green hornets.jpg"
    else:
        team, img = "UNASSIGNED", ""

    out.innerHTML = f"✅ YOU ARE ELIGIBLE!<br>TEAM: <span style='color:#ffd400'>{team}</span>"
    if img:
        img_box.innerHTML = f"<img src='{img}' class='team-img'>"