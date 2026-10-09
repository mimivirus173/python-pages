import random
from pyscript import web, when

output_text = None
@when("click", "#submit-button")
def roll(event):
    # Get the number input
    num_input = web.page["num_input"]
    num = int(num_input.value)

    if num <= 99 and num > 0:
        # Random number
        roll = random.randint(1, 100)

        # Win/Loss
        if roll >= num:
            output_text = f"You win!\nThe random number was {roll}"
        else:
            output_text = f"You lose!\nThe random number was {roll}"
    else:
        output_text = "Invalid input"

    # Update the output text on the page
    output_div = web.page["output"]
    output_div.innerText = output_text