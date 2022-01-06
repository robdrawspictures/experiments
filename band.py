def message(name, artist):
    if artist == "Suede":
        print(f"Hey, {name}, you have great taste! {artist} are the best!")
    else:
        print(f"So you like {artist}, {name}? That's nice.")

name_1 = input("What's your name, friend? ")
artist_1 = input("What's your favourite band or artist? ")
output = message(name_1, artist_1)
print(output)