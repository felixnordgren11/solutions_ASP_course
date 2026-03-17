from .die import Die
from .utils import i_just_throw_an_exception


class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        #self.reset()
        self.round = 1
        self.wins = 0
        self.loses = 0


    #def reset(self):
    #    self.round = 1
    #    self.wins = 0
    #    self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += 1 * die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        

        runner = cls()
        while True:


            print("Round {}\n".format(runner.round))
            
            for die in runner.dice:
                die.roll()
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                print(f"runner.wins = {runner.wins}")
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
            print("Wins: {} Losses: {}".format(runner.wins, runner.loses))
            runner.round += 1
            
            if runner.wins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break
            
            prompt = input("Would you like to play again?[Y/n]: ")
            print(f"runner.wins = {runner.wins} end of loop")
            print(f"runner.loses = {runner.loses} end of loop")
            
            if prompt == 'y' or prompt == '':
                continue
            else:
                i_just_throw_an_exception()
