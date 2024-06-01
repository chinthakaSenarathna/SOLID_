class DatabseWriter:
    def __init__(self, database) -> None:
        self.databse = databse

    def write(self, record: tuple):
        try:
            self.databse.write(record)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {e}")
