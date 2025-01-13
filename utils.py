from concurrent.futures import ThreadPoolExecutor
from rich.console import Console
from rich.markdown import Markdown



def thread(func, args: list=[], max_workers: int=10):
    # thread pool executor map
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(func, args))

def retry(func, tries=3, func_args: tuple = (), exceptions: tuple = (Exception,)):
    """
    A utility function to retry a function multiple times if it raises any exceptions.

    :param func: The function to retry.
    :param tries: The number of times to retry the function.
    :param func_args: The arguments to pass to the function.
    :param exceptions: A tuple of exceptions to catch.
    :return: The result of the function.
    """
    for attempt in range(tries):
        try:
            print(f"Attempt {attempt + 1} of {tries}")
            return func(*func_args)
        except exceptions as e:
            if attempt == tries - 1:
                raise
            else:
                print(f"Exception occurred: {e} - Retrying...")
                continue


def not_none(data, type):
    if isinstance(data, str) and len(data.strip()) == 0:
        return False
    elif isinstance(data, type) and len(data) != 0:
        return True
    else:
        return False


def md_print(text: str):
    # rich markdown print
    console = Console()
    console.print(Markdown(text))
