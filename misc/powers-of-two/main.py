from pyscript import web, when

# Initial empty list display text that i should move to the html file later
output_text = f"<br>[]"
output_div = web.page["output"]
output_div.innerHTML = output_text

@when("click", "#submit-button")
def pot(event):
    # Get the number input
    num_input = web.page["num_input"]
    num = int(num_input.value)

    # Append the powers of two up to {num} in a list
    powers = []
    for i in range(1, num + 1):
        powers.append(2**i)

    output_text = (
        f"<br><div id='output'>{powers}</div>"
    )

    # Update the output text on the page
    output_div = web.page["output"]
    output_div.innerHTML = output_text