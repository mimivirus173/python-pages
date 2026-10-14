import random
from pyscript import web, when

points = 0
highscore = 0
output_text = None
@when("click", "#submit-button")
def roll(event):
    global points
    global highscore
    
    # Get the number input
    num_input = web.page["num_input"]

    try: # Check if num is int
        num = int(num_input.value)
        
        # Check if input is in the valid range
        if 0 < num <= 99:
            roll_val = random.randint(1, 100)
            if roll_val >= num:
                points += num

                if points > highscore:
                    highscore = points
                
                output_text = (
                    f"<b>You win!</b><br>"
                    f"The random number was {roll_val}.<br><br>"
                    f"You gain {num} points.<br>"
                    # f"Your current points are <b>{points}</b>."
                )
            else:
                output_text = (
                    f"<b>You lose!</b><br>"
                    f"The random number was {roll_val}.<br><br>"
                    f"Final score: <b>{points}</b>"
                )
                points = 0
        else:
            output_text = (
            f"<b>Invalid input!</b><br>" 
            f"Input must be between 1 and 99."
        )

    except ValueError:
        output_text = (
            f"<b>Invalid input!</b><br>" 
            f"Please enter a valid integer."
        )

    # Update text on the page
    # Text below the input box
    output_div = web.page["output"]
    output_div.innerHTML = output_text

    # Score counter
    header_div = web.page["header"]
    header_div.innerHTML = f"Score: <b>{points}</b> High score: <b>{highscore}</b>"