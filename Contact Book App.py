from spellchecker import SpellChecker

# Step 1: Create the SpellCheckerApp class
class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    # Step 2: Text correction logic
    def correct_text(self, text):
        words = text.split()
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'Correcting "{word}" to "{corrected_word}"')
            corrected_words.append(corrected_word)

        return ' '.join(corrected_words)

    # Step 3: Run the main loop
    def run(self):
        print("\n--- Spell Checker ---")
        while True:
            text = input("Enter text to check (or type 'exit' to quit): ")
            if text.lower() == "exit":
                print("Exiting Spell Checker. Goodbye!")
                break
            corrected = self.correct_text(text)
            print(f"✅ Corrected Text: {corrected}")

# Step 4: Main program entry point
if __name__ == "__main__":
    SpellCheckerApp().run()
