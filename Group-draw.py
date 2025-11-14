import random
import datetime

def create_teams(n):
    """
    Randomly assigns 'n' players (numbered 1 to n) into two teams: Red and Green.

    :param n: The total number of players.
    :return: A dictionary containing the date and the two teams.
    """
    if n <= 1:
        print("Error: You need at least 2 players to form two teams.")
        return None

    # 1. Get the list of players (numbers 1 to n)
    players = list(range(1, n + 1))
    
    # 2. Randomly shuffle the list of players
    random.shuffle(players)
    
    # 3. Determine the split point. 
    # If n is odd, the 'red' team will have one extra player.
    midpoint = (n + 1) // 2 
    
    # 4. Split the shuffled list into two teams
    red_team = players[:midpoint]
    green_team = players[midpoint:]
    
    # 5. Get the current date
    #today = datetime.date.today().strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M%S")
    
    return {
        "date": today,
        "red_team": red_team,
        "green_team": green_team
    }

def main():
    """
    Main function to handle user input and display the results.
    """
    print("--- Soccer Team Grouping Tool ---")
    
    while True:
        try:
            # Get user input for the number of people
            n_input = input("Enter the total number of players (N): ")
            n = int(n_input)
            
            if n <= 1:
                print("Please enter a number of players greater than 1.")
            else:
                break
        except ValueError:
            print(f"Invalid input: '{n_input}'. Please enter a whole number.")
            
    # Generate the teams
    result = create_teams(n)
    
    if result:
        print("\n" + "="*40)
        print(f"Date: {result['date']}")
        print(f"Total Players: {n}")
        print("="*40)
        
        # Display the teams
        print(f"🔴 RED TEAM ({len(result['red_team'])} Players):")
        print(", ".join(map(str, result['red_team'])))
        print("-" * 40)
        
        print(f"🟢 GREEN TEAM ({len(result['green_team'])} Players):")
        print(", ".join(map(str, result['green_team'])))
        print("="*40)

if __name__ == "__main__":
    main()