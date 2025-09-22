fifi
from pyscript import document, display


def generate_message(e): #we put e for event handling
    #to get the value from what we input
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    #multiline string
    profile = f"""
﹒୨𝑒   ﾟ ˖Student Profile﹒୨𝑒   ﾟ ˖  ⠀
    Name    : {name}
    Age     : {age}
    School  : {school}

Notes:
    {name} is currently {age} years old and studies at {school}.\nThis information was gathered through input fields and displayed\nusing a multiline string in Python via PyScript.
    """

    document.getElementById("message").innerText = profile