from pyscript import web, when

@when("click", "#submit-button")
def roll(event):
    num_input = web.page["num_input"]
    num = num_input.value
    
    output_div = web.page["output"]
    output_div.innerText = num.value