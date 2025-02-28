# Define the VotingSystem class
class VotingSystem:
    def __init__(self):
        self.candidates = {}
    
    def add_candidate(self, name):
        if name in self.candidates:
            print(f"Candidate '{name}' is already in the system.")
        else:
            self.candidates[name] = 0
            print(f"Candidate '{name}' has been added.")
    
    def show_candidates(self):
        if not self.candidates:
            print("No candidates available.")
        else:
            print("Candidates:")
            for candidate in self.candidates:
                print(f"- {candidate}")
    
    def vote_to_candidate(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            print(f"Vote casted for '{name}'.")
        else:
            print(f"Candidate '{name}' does not exist.")
    
    def get_results(self, name):
        if name in self.candidates:
            print(f"Candidate '{name}' has {self.candidates[name]} votes.")
        else:
            print(f"Candidate '{name}' does not exist.")
    
    def display_winner(self):
        if not self.candidates:
            print("No candidates available.")
        else:
            winner = max(self.candidates, key=self.candidates.get)
            votes = self.candidates[winner]
            print(f"The winner is '{winner}' with {votes} votes.")

voting_system = VotingSystem()

# Add candidates
voting_system.add_candidate("Ali")
voting_system.add_candidate("Shahd")
voting_system.add_candidate("Nancy")

# Show candidates
voting_system.show_candidates()

#  votes
voting_system.vote_to_candidate("Ali")
voting_system.vote_to_candidate("Shahd")
voting_system.vote_to_candidate("Nancy")

#  results for specific candidates
voting_system.get_results("Ali")
voting_system.get_results("Nancy")

# Display the winner
voting_system.display_winner()
