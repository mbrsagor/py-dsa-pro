class SongNode(object):    def __init__(self, current_song=None, next_song=None):        self.current_song = current_song        self.next_song = next_songclass SongList(object):    def __str__(self):        self.head = None        self.size = 0    def display(self):        value = self.head        while value:            print(value.current_song)            value = value.next_song    def insert(self, value):        song_node = SongNode(value)        if self.head is None:            self.head = song_node        last = self.head        while last.next_song:            last = last.next_song        last.next_song = song_node    def getsize(self):        passsong_list = SongList()song_list.head = SongNode('I love you')second = SongNode('Oh! my darling I love you')third = SongNode("Let me love you")song_list.head.next_song = secondsecond.next_song = thirdsong_list.display()song_list.insert('We are not alone')song_list.insert('O god love us love us')song_list.display()