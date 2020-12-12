artists = ['Taylor Swift', 'Matthew Patrick Alwyns']   # container data type
# print(artists)

# CRUD
# Create
artists.append('Alec Benjamin')
print(artists)

# Read
music_industry = artists[0]
print(f'{music_industry} is the music industry')
# print(len(artists))
for i in range(len(artists)):
    print(f'{i + 1}. {artists[i]}')

# Update
artists[1] = 'Joe Alwyns'

# Delete
# artists.pop(1)     # delete by index
deleted_artist = artists.pop(1)    # delete by index and assign
print(deleted_artist)

# find index by value
# print(artists.index('Taylor Swift'))
if 'Gigi Hadid' in artists:
    print(artists.index('Gigi Hadid'))