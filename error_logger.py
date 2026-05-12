from datetime import datetime


def log_error(error, location):
    # Save error details inside errors.log file
    try:
        file = open("errors.log", "a")

        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_type = type(error).__name__
        error_message = str(error)

        line = f"{date_time} | {error_type} | {error_message} | {location}\n"

        file.write(line)
        file.close()

    except Exception:
        # If logging fails, do not crash the program
        pass