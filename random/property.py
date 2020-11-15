class Bangladesh(object):

    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if new_score <= 0:
            raise ValueError("Score can't be negative value")
        else:
            self._score = new_score


bd = Bangladesh()
bd.score = 300
print(bd.score)
