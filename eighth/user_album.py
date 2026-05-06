# 8-8. User Albums: Start with your program from Exercise 8-7 . Write a while 
# loop that allows users to enter an album’s artist and title . Once you have that 
# information, call make_album() with the user’s input and print the dictionary 
# that’s created . Be sure to include a quit value in the while loop.
def make_album(artist_name, album_title, number_of_tracks=''):
    music_album = {}
    music_album["artist_name"] = artist_name
    music_album["album_title"] = album_title
    if number_of_tracks:
        music_album["number_of_tracks"] = number_of_tracks
    return music_album

message = ''
while message!=quit:
    print("\nWelcome to the album maker! We'll ask you basic information about it!")
    print("Enter 'quit' in any point to exit.")
    artist_name = input("\nEnter the artist's name: ")
    if artist_name == 'quit':
        break
    album_title = input("Enter the album's title: ")
    if album_title == 'quit':
        break
    includes_track_number = input("Would you like to specify how many tracks does the album have? (Y/N): ")
    if includes_track_number == 'quit':
        break
    if includes_track_number.lower() == 'y':
        tracks = input("Enter the album's number of tracks: ")
        if tracks == 'quit':
            break
        print(make_album(artist_name, album_title, tracks))
        continue
    print(make_album(artist_name,album_title))
