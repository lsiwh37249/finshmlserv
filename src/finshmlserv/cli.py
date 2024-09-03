import typer
#from finshmlserv.model.manager import get_model_path
import pickle

app = typer.Typer()

def ping():
    return pong

def get_model_path():
    from finshmlserv.model.manager import get_model_path
    return get_model_path()


def run_prediction(
        l: float = typer.Option(show_default=False),
        w: float = typer.Option(show_default=False)
        ):
    path = get_model_path()
    with open(path, "rb") as f:
        fish_model = pickle.load(f)
    prediction = fish_model.predict([[l, w]])

    fish_class = " "
    if prediction[0] == 1:
        fish_class = "도미"
    else:
        fish_class = "우럭"

    print(fish_class)
    
#@app.command()
def prediction():
    typer.run(run_prediction)

#if __name__ == "__main__":
#    app()
