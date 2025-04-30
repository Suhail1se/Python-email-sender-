class DivisionError(Exception):
    pass

def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise DivisionError("Cannot divide by zero.")
        return a / b
    except ValueError:
        log_error("Invalid input type.")
        return "Invalid input type."
    except DivisionError as e:
        log_error(str(e))
        return str(e)
    except Exception as e:
        log_error(f"Unexpected error: {str(e)}")
        return "An unexpected error occurred."

def log_error(message):
    with open("error_log.txt", "a") as f:
        f.write(message + "\n")
