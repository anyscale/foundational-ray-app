import inspect

from IPython.display import Markdown, display


def show(func):
    try:
        display(Markdown(f"```python\n{inspect.getsource(func)}\n```"))
    except Exception as e:
        print(f"Error: {e}")
