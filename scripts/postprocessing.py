import re
from io import StringIO
from contextlib import redirect_stdout



def run_python(text):
    copy = False
    block = ""
    out = ""
    for line in text.split("\n"):
        # print(f"line: {line}")
        out += f"{line}\n"
        if line.strip() == "```python":
            print("starting block")
            copy = True
        elif line.strip() == "```":
            print("ending block")
            copy = False
            # print("__________")
            # for x in block.split("\n"):
            #     print(f">{x}<")
            # print("__________")
            result = evaluate(block)
            print(f"{result = }")
            out += f"Result: {result}\n"
            block = ""
        elif line.startswith("#"):
            print("ignoring comment")
            block += "\n"

        elif copy:
            block += f"{line}\n"
        
    return out

def evaluate(code):
    # return eval(code)
    f = StringIO()
    with redirect_stdout(f):
        exec(code)
    return f.getvalue()
    try:
        f = StringIO()
        with redirect_stdout(f):
            eval(code)
        return f.getvalue()
    except Exception as e:
        print(e)
        return "<Error evaluating code>"