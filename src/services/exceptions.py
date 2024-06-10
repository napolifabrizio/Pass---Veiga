import traceback

def treat_exception(e, local):
    print(f'Aconteceu um erro desconhecido no {local}: {e}')
    print(traceback.format_exc())