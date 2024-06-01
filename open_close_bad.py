class Writer:
    def __init__(self, type: int) -> None:
        self.type = type
        # we have to create socket              -> Network
        # we have to create database connection -> Databse
        # but, sometime we not used it
        

    def write(self, contents: bytearray):
        if(self.type == 0): # File Writer
            with open("random_file.txt", "w") as output_file:
                output_file.write(contents)

        elif(self.type == 1): #Network Writer
            self.some_socket.write(contents)

        elif(self.type == 2): # Databse
            self.db.write(contents)


file_writer = Writer(type = 0)
Network_writer = Writer(type = 1)
