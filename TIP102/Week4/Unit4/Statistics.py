'''
Understand: Obtain the average value of the NFTs, if the collection is empty return average 0
Plan: Keep track of total value and return average as total divided by the length of the dictionary
'''
def average_nft_value(nft_collection):
    if len(nft_collection) < 1:
        return 0
    total = 0
    for nft in nft_collection:
        total += nft["value"]
    return total / len(nft_collection)
# Test Cases
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))
