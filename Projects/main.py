from dog import Dog


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

my_dog = GoldenRetriever("Rufus", 3)
print(my_dog.speak())