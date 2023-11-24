
def process(text: str = "",variables: dict={}):
    for key in variables.keys():
        text = text.replace(f"${key}", str(variables[key]))
    import arrow
    now = arrow.now()
    date = now.format('YYYY-MM-DD HH:mm:ss')
    text = text.replace("$date", date )




    return text

# UNUSED

if __name__ == "__main__":
    print(process(text="$date"))