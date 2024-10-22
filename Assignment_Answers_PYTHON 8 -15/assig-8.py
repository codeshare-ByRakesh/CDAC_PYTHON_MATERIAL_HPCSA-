#  Voting System for Favorite Movies

def manage_votes():

    votes = {}

    while True:
        print("\nOptions:")
        print("1. Add a new movie")
        print("2. Vote for a movie")
        print("3. Remove a movie")
        print("4. Display voting results")
        print("5. Find the top movie")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            movie = input("Enter the movie name to add: ")
            if movie not in votes:
                votes[movie] = 0
                print(f"Added '{movie}' to the voting list.")
            else:
                print(f"'{movie}' is already in the voting list.")

        elif choice == '2':
            movie = input("Enter the movie name to vote for: ")
            if movie in votes:
                votes[movie] += 1
                print(f"Voted for '{movie}'. Total votes: {votes[movie]}")
            else:
                print(f"'{movie}' is not in the voting list.")

        elif choice == '3':
            movie = input("Enter the movie name to remove: ")
            if movie in votes:
                del votes[movie]
                print(f"Removed '{movie}' from the voting list.")
            else:
                print(f"'{movie}' is not in the voting list.")

        elif choice == '4':
            if votes:
                print("Voting results:")
                for movie, count in votes.items():
                    print(f"{movie}: {count} votes")
            else:
                print("No movies in the voting list.")

        elif choice == '5':
            if votes:
                top_movie = max(votes, key=votes.get)
                print(f"The top movie is '{top_movie}' with {votes[top_movie]} votes.")
            else:
                print("No movies in the voting list.")

        elif choice == '6':
            print("Exiting the voting system.")
            break

        else:
            print("Invalid choice. Please try again.")


manage_votes()
