import requests
import random
import enquiries

api = requests.get("https://api-escapamet.vercel.app")

class Memorias:

    def __init__(self):
        self.grid = [['😀','🙄','🤮','🥰'],['🤮','😨','🤓','😷'],['😨','🤓','🥰','😷'],['🤑','🤑','🙄','😀']]
        self.shuffle_grid = []
        self.shuffle()
        self.guess_grid = []
        self.guess()
        self.get_length()
    
    
 

    def shuffle(self):
        temp_grid = random.sample(self.grid, len(self.grid))
        for lists in temp_grid:
            shuffled_row = random.sample(lists, len(lists))
            self.shuffle_grid.append(shuffled_row)


    def guess(self):
        for lists in self.shuffle_grid:
            self.guess_grid.append([])
            for emoji in lists:
                emoji = "?"
                self.guess_grid[-1].append(emoji)


    def get_length(self):
        return len(self.grid)

    def coordinates(self):
        length_options = self.get_length()
        options = [x for x in range(1,length_options+1)]
        coordinate_x = enquiries.choose("Escoje una fila: ", options)
        coordinate_y = enquiries.choose("Escoje una columna: ", options)
        return coordinate_x, coordinate_y
    
    
    def guess_card(self):
        while True:
            x, y = self.coordinates()
            self.guess_grid[x-1][y-1] = self.shuffle_grid[x-1][y-1]
            self.show_grid()
            x2, y2 = self.coordinates()
            while x2 == x and y2 == y:
                print("Debes escoger otra casilla.")
                x2, y2 = self.coordinates()
            if self.shuffle_grid[x2-1][y2-1] == self.shuffle_grid[x-1][y-1]:
                self.guess_grid[x2-1][y2-1] = self.shuffle_grid[x2-1][y2-1]
                self.show_grid()
                print("Match!")
            else:
                self.guess_grid[x-1][y-1] = "?"
                print("No match.")


memoria = Memorias()
memoria.coordinates()