# Name: Blake Mann
# PSID: 1832387
class Team:


    def __init__(self, team_name='None', team_wins = 0, team_losses = 0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
       return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses


    if team.get_win_percentage() >= .5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name,'has a losing average.')
