"""
Classes developed by Sebastián Romero Cruz, a
professor at NYU Tandon School of Engineering
"""

from enum import Enum
from sys import stdout
from time import sleep
from random import choice
from os import system, name


class Direction(Enum):
    """
    Representing each of the directions the game can display to the user.
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class DanceDanceRevolution:
    _ARROWS = {
        Direction.UP: """
        -------------------
        -------------------
        ---------x---------
        --------/ \--------
        -------/   \-------
        ------/     \------
        -----/—+   +—\-----
        -------|   |-------
        -------+———+-------
        -------------------
        -------------------
        """,
        Direction.LEFT: """
        -------------------
        -----x-------------
        ----/|-------------
        ---/ |-------------
        --/  +——————————+--
        -x              |--
        --\  +——————————+--
        ---\ |-------------
        ----\|-------------
        -----x-------------
        -------------------
        """,
        Direction.RIGHT: """
        -------------------
        -------------x-----
        -------------|\----
        -------------| \---
        --+——————————+  \--
        --|              x-
        --+——————————+  /-
        -------------| /---
        -------------|/----
        -------------x-----
        -------------------
        """,
        Direction.DOWN: """
        -------------------
        -------------------
        -------+———+-------
        -------|   |-------
        -----\—+   +—/-----
        ------\     /------
        -------\   /-------
        ------- \ /--------
        ---------x---------
        -------------------
        -------------------
        """
    }
    _STR_TO_DIRECTION = {
        'U': Direction.UP,
        'D': Direction.DOWN,
        'L': Direction.LEFT,
        'R': Direction.RIGHT
    }

    @staticmethod
    def clear_console() -> None:
        """
        Clears any contents currently on the user's terminal display,
        """
        system('clear' if name == 'posix' else 'CLS')

    def __init__(self) -> None:
        """
        Constructor for the DanceDanceRevolution class. Gives speed and amount the default values of 1, and initialises
        the list of steps as an empty list.

        Be aware that all instances of the DanceDanceRevolution class will share the same list (i.e. they are all shallow
        copies of each other). Love Python's memory model.
        """
        self._speed: float = 1
        self._amount: int = 1
        self._steps: list[Direction] = []

    def set_speed(self, speed: float) -> None:
        """
        Sets the speed of the game, which is by default 1.

        Args:
            speed (float): A numerical value representing the desired speed at which the game will run

        Raises:
            TypeError: If the user does not enter a numerical value (i.e. a float or an int)
            ValueError: If the user enters a negative number or zero
        """
        if not isinstance(speed, float) and not isinstance(speed, int):
            raise TypeError("Speed must be a positive numerical value.")
        
        if speed <= 0:
            raise ValueError("Speed must be a positive numerical value.")

        self._speed = speed

    def set_amount(self, amount: int) -> None:
        """
        Sets the amount of steps that will be displayed by the game, which is by default 1.

        Args:
            amount (int): An integer value representing the desired amount of steps that will be displayed by the game

        Raises:
            TypeError: If the user does not enter an integer value
            ValueError: If the user does not enter a positive non-zero value for the amount
        """
        if not isinstance(amount, int):
            raise TypeError("Amount of steps must be a positive int value.")
        
        if amount <= 0:
            raise ValueError("Amount of steps must be a positive int value.")

        self._amount = amount

    def play_sequence(self) -> None:
        """
        Runs our memory game under the current speed and amount of steps set up by the game. Each turn, the game
        will choose a random ASCII art arrow and display it to the user. After a short amount of time (determined
        by the inverse of the set speed), the game will clear the screen and display the next arrow.

        The game will keep track of the sequence of directions being displayed so that the user can later check
        their answers using check_answers().
        """
        # If we're playing the game for a second time, remove the answers from the previous round
        if len(self._steps) != 0:
            self._steps.clear()

        keys: list[Direction] = list(DanceDanceRevolution._ARROWS.keys())
        previous_direction: Direction = None

        # For every step of the game
        for _ in range(self._amount):
            random_direction = choice(keys)         # choose a random direction

            while random_direction == previous_direction:
                random_direction = choice(keys)     # make sure it is not the same direction as the previous one
            
            previous_direction = random_direction

            self._steps.append(random_direction)    # record it
            self._draw_arrow(random_direction)      # draw it

            sleep(1.0 / self._speed)                # sleep for a bit
            DanceDanceRevolution.clear_console()    # and clear the console
    
    def check_answers(self, answers) -> bool:
        """
        Given a list of strings representing a player's answers, will return True if the answers match the game's
        latest run's sequence of directions. Returns False otherwise.

        Args:
            answers (list[str]): Represents the user's answers

        Raises:
            TypeError: If the user passes a non-list object or an empty list object
            TypeError: If any of the user's answers are, for any reason, not str objects

        Returns:
            bool: Whether or not the user got all steps correct
        """
        if not isinstance(answers, list) or len(answers) == 0:
            raise TypeError("Answers must be passed in as a non-empty list of str objects.")
        
        if len(answers) != len(self._steps):
            return False

        for index, answer in enumerate(answers):
            if not isinstance(answer, str):
                raise TypeError(f"Answer #{index + 1}, '{answer}', is not a str object. Answers must be passed in as a list of str objects.")
            
            current_correct_step = self._steps[index]

            # the answer is incorrect if the letter is not even one of the directions or if it does not match the correct answer
            if answer not in DanceDanceRevolution._STR_TO_DIRECTION or DanceDanceRevolution._STR_TO_DIRECTION[answer] != current_correct_step:
                return False
        
        return True
    
    def _draw_arrow(self, direction: Direction) -> None:
        """
        Clears the user's console and draws the specified arrow using ASCII art.

        Args:
            direction (Direction): The desired arrow to be drawn (see _ARROWS above)

        Raises:
            TypeError: If the user doesn't enter a Direction enum to determine the direction of the arrow
        """
        if not isinstance(direction, Direction):
            raise TypeError("Arrow direction must be a Direction type enum.")

        # Clear the console
        DanceDanceRevolution.clear_console()

        # Write the current frame on stdout and sleep
        stdout.write(DanceDanceRevolution._ARROWS[direction])
        stdout.flush()


if __name__=='__main__':
    ddr = DanceDanceRevolution()
    ddr.set_amount(5)
    ddr.set_speed(2)
    ddr.play_sequence()
