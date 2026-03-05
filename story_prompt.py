import random

characters = ["a curious turtle", "a brave rabbit", "a tiny astronaut", "a clever fox"]
places = ["in a magical forest", "on a faraway planet", "near a quiet river", "inside a hidden cave"]
challenges = [
    "finds a mysterious map",
    "must help a lost bird",
    "discovers a glowing door",
    "tries to solve a magical puzzle"
]

character = random.choice(characters)
place = random.choice(places)
challenge = random.choice(challenges)

story_prompt = f"Story Idea: {character} {place} who {challenge}."

print(story_prompt)
