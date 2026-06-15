def generate_band_name(city, pet):
    return f"{city} {pet}s"

city = input("Enter your city: ")
pet = input("Enter your pet's name: ")

band_name = generate_band_name(city, pet)
print(f"\n🎵 Your band name could be: {band_name}")