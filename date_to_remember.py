import streamlit as st

def display_ascii_art(art):
    """Displays ASCII art passed as a parameter."""
    print(art)

def game_intro():
    """Introduction to the game."""
    print("Welcome to the Virtual Date Adventure!")
    print("You're about to relive an unforgettable first date at a cozy restaurant.")
    print("Every choice you make shapes the story, so choose wisely.")
    input("Press Enter to begin your adventure...")

def make_choice(prompt, options):
    """
    Prompts the player with a question and returns their choice.
    
    Parameters:
    - prompt: The question to ask the player.
    - options: A dictionary of valid options (e.g., {"1": "Option 1 text", "2": "Option 2 text"}).
    
    Returns:
    - The key corresponding to the player's choice.
    """
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice: ")
    while choice not in options:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ")
    return choice

def game():
    """Main game function."""
    game_intro()

    # Scene 1: Arrival at the Restaurant
    prompt = "You walk into the restaurant and spot Eric sitting at a cozy table near the window. What do you do?"
    options = {
        "1": "Smile, wave and walk over with to Eric.",
        "2": "Look at yourself with your camera to make sure you're ready, then compose yourself and head over confidently.",
        "3": "Surprise him by sneaking up quietly to the table."
    }
    choice = make_choice(prompt, options)
    if choice == "1":
        print("Eric waves back, smiling warmly as you approach.")
    elif choice == "2":
        print("You take a deep breath, then walk over with poise. Eric smiles immensely!")
    elif choice == "3":
        print("He’s caught off guard but laughs, clearly charmed by your playful entrance and astonishing looks.")

    # Scene 2: Breaking the Ice
    prompt = "The conversation starts easily. What topic do you bring up first?"
    options = {
        "1": "Ask him how his day has been so far.",
        "2": "Talk about the cozy ambiance of the restaurant.",
        "3": "Bring up that it's about time that we met up."
    }
    choice = make_choice(prompt, options)
    if choice == "1":
        print("He shares a bit about his day, and the conversation flows naturally.")
    elif choice == "2":
        print("He agrees, pointing out the amazing smell of the food that's being cooked and the beautiful sight that's in front of him.")
    elif choice == "3":
        print("He agrees that it is about time and can't stop smiling. The mood becomes even more relaxed and fun.")

    # Scene 3: The Dinner
    prompt = "As we order our food, talk, and then dinner arrives, the conversation deepens. What do you ask him about?"
    options = {
        "1": "His favorite thing that he has done on Christmas break.",
        "2": "A funny or embarrassing memory from his childhood or from his years in college.",
        "3": "What he’s looking forward to most this holiday season."
    }
    choice = make_choice(prompt, options)
    if choice == "1":
        print("He shares a few heartwarming stories about family, and you find yourself smiling the whole time.")
    elif choice == "2":
        print("His story has you both laughing, making you realize that he's opening up to you.")
    elif choice == "3":
        print("His answer about what he wanted this holiday season reveals how much he values meaningful connections like the one he managed to get through tiktok, of all places.")

    # Scene 4: The Gesture
    prompt = "As the evening winds down, he seems a little fidgety, like he’s planning something. What do you do?"
    options = {
        "1": "Playfully ask if he’s nervous about something.",
        "2": "Wait patiently, feeling curious to see what might happen next.",
        "3": "Lean in closer, noticing the glimmer of excitement in his brown eyes."
    }
    choice = make_choice(prompt, options)
    if choice == "1":
        print("He laughs nervously and says, 'You’ll see soon enough!'")
    elif choice == "2":
        print("You wait, feeling the anticipation build as he reaches into his pocket.")
    elif choice == "3":
        print("He grins, clearly happy that you’re just as curious as he is.")

    # Final Scene: The Big Reveal
    print("As the conversation pauses, he suddenly pulls something from his pocket.")
    print("With a warm smile, he holds it above you, and you look up to see...")

    
    mistletoe_art = """
       ____
     {0  0}
      \__/
       |||
      /   \\
     |_____|
    """
    
    display_ascii_art(mistletoe_art)

    print("A mistletoe, dangling playfully above you.")
    print("Your cheeks flush as you meet his gaze, and you both share a smile.")
    print("He leans closer, and the moment becomes magical. The End.")

# Run the game
if __name__ == "__main__":
    game()
