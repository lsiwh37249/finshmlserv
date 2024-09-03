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
    """주어진 물고기의 길이(l)와 무게(w)를 기반으로 해당 물고기의 종류를 예측하는 함수.

    매개변수:
    l (float): 물고기의 길이.
    w (float): 물고기의 무게.

    반환값:
    str: 예측된 물고기의 종류로, '도미' 또는 '우럭' 중 하나를 반환.

    동작:
    1. 사전 학습된 모델의 경로를 가져온다.
    2. 해당 경로에서 모델을 불러온다.
    3. 불러온 모델을 사용하여 주어진 길이와 무게에 대해 예측을 수행한다.
    4. 예측 결과에 따라 '도미' 또는 '우럭'을 반환한다.
    """

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
    
def prediction():
    typer.run(run_prediction)
