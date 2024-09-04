def get_model_path(neighbor):
    import os 
    # 이 함수 파일의 절대경로를 받아온다. 
    #print(os.path.abspath(__file__))
    #path = os.path.abspath(__file__)

    #model_path = path[:-10]+"model.pkl"
    #강사님 코드 -> dirname를 사용했다.
    my_path = __file__
    dir_name = os.path.dirname(my_path)
    model_path = os.path.join(dir_name, f"model{neighbor}.pkl")

    return model_path
