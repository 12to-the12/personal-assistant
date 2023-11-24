from scripts.substitute_variables import process

def test_say():
    result = process("this is the current date:$date.")
    

    import arrow
    now = arrow.now()
    date = now.format('YYYY-MM-DD')

    assert result == f"this is the current date:{date}."