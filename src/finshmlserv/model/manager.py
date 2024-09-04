def get_model_path(neighbor):
    import os 
    my_path = __file__
    dir_name = os.path.dirname(my_path)
    model_path = os.path.join(dir_name, f"model{neighbor}.pkl")

    return model_path
