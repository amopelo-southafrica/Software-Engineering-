class Album:
    def __init__(self, album_name,number_of_songs,album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
        pass
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"
        pass
    
    def __repr__(self):
        return self.__str__()

album1 = [Album("DAMN", "Kendrick Lamar", 14),Album("Thriller", "Michael Jackson", 9),Album("The Dark Side of the Moon", "Pink Floyd", 10),Album("Take Care", "Drake", 18),Album("Back to Black", "Amy Winehouse", 11)]
sorted_list = sorted(album1,key=lambda album: album.number_of_songs)
sorted_list[0]= sorted_list[1]
print(sorted_list[0])

album2= [Album("To Pimp a Butterfly", "Kendrick Lamar", 16),Album("Abbey Road", "The Beatles", 17),Album("Graduation", "Kanye West", 13),Album("21", "Adele", 11),Album("Astroworld", "Travis Scott", 17)]
print(album2)
album2.extend(album1)
new1 = [Album("The Dark Side of the Moon", "Pink Floyd", 9) , Album("Oops!I Did It Again", "Britney Spears", 16)]
album2.extend(new1)
print(album2)

sorted_1= sorted(album2,key=lambda album :album.album_name)
print(sorted_1)


target_item = Album("The Dark Side of the Moon", "Pink Floyd", 9)

def sequential_search(target_item, album2): 
    for index in range(len(album2)): 
        for search in range(index):
            if album2[index] == target_item: 
                return index 
            else:
                return None 

result = sequential_search(target_item, album2) 
 
if result is not None: 
    print(f"Item {target_item} found at index {result}.") 
else: 
    print(f"Item {target_item} not found in the list.") 