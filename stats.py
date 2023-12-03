


class Stats():
    """statistik ma’lumotlarni kuzatib boradi!"""

    def __init__(self):
        """statistikani initsializatsiya qiladi."""
        self.guns_left = 3
        self.run_game = True
        self.score = 0
        with open('records.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset(self):
        """uyn vaqida statistikani uzgartirish!!"""
        

