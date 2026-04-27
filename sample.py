import modal

app=modal.App("getting started")

@app.function()
def square(x):
    print("This is a remote worker")
    return x**2

@app.local_entrypoint()
def main():
    print("The square is",square.remote(24))