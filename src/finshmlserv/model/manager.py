def get_model_path():
    import os 
    # 이 함수 파일의 절대경로를 받아온다. 
    #print(os.path.abspath(__file__))
    path = os.path.abspath(__file__)
    model_path = path[:-10]+"model.pkl"
    
    return model_path
