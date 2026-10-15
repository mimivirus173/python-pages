from pyscript import web, when

count = 0

@when("click", "#clicker")
def iterate(event):
    global count
    count += 1

    web.page["count"].innerHTML = count