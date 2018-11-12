class Grzegorz:
    """Main class"""
    def __init__(self):
        print("zadanie staz")
    def read(self):
        print("otwieranie i zamykanie pliku")
        text_file = open("piotr.txt","r")
        lines = text_file.readlines()
        for line in lines:
            for word in line.split():
                print(word)
                
            
        
        
        
piotr = Grzegorz()
piotr.read()

