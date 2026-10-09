import random
from pyscript import web, when

points = 0
output_text = None
@when("click", "#submit-button")
def roll(event):
    global points # Declare points as global so its value persists
    
    # Get the number input
    num_input = web.page["num_input"]
    num = int(num_input.value)

    # Check if input is in the valid range
    if num <= 99 and num > 0:
        # Random number
        roll = random.randint(1, 100)

        # Win/Loss
        if roll >= num:
            points += num

            output_text = (  f"<b>You win!</b>"
                           + f"<br>The random number was {roll}."
                           + f"<br><br>You gain {num} points."
                           + f"<br>Your current points are <b>{points}</b>."
                        )
        else:
            output_text = (  f"<b>You lose!</b>"
                           + f"<br>The random number was {roll}."
                           + f"<br>Your total points were <b>{points}</b>."
                        )
            points = 0
    else:
        output_text = "Invalid input"

    # Update the output text on the page
    output_div = web.page["output"]
    output_div.innerHTML = output_text