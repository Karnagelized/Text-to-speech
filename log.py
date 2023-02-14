
import os
import time

def log_write(error) -> None:
    log_directory = 'log'

    if log_directory not in os.listdir():
        os.makedirs(log_directory)

    with open(f"{log_directory}/{time.strftime('Error %Y-%m-%d %H-%M-%S')}.txt", 'w+') as log_file:
        error_text = (
            'Program have a Error, please contact the developer to solve this problem!' +
            '\nError name:'
            f'\n{error}' +
            '\n\nDeveloper contact:' +
            '\nVK - https://vk.com/masikantonov'
            '\nGit - https://github.com/Karnagelized'
        )

        log_file.write(error_text)
