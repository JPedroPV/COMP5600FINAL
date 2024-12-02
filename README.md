<!-- Project Title -->
<br />
<div align="center">
  <h3 align="center">Supreme Sudoku Solver!</h3>

  <p align="center">
    A application to create sudoku boards, play sudoku, and test the efficacy of Constrain Satisfaction Problem algorithms such as Most Constrained Value, Forward-Checking, and Arc Consistency
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

This application can be run by installing the packages with the following.
* npm
  ```sh
  pip install requirements.txt
  ```
  Next you'd want to make sure you have sudoku.csv (not sudokuMini.csv) if it wasn't already included with this copy of the program you can find it here:
  [https://www.kaggle.com/datasets/rohanrao/sudoku](https://www.kaggle.com/datasets/rohanrao/sudoku)

  Finally, to run the program, run:
  ```sh
  python3 main.py
  ```

This program has the ability to run 3 different programs depending on a user inputing 1, 2, or 3, respectively.
* (1) Will allow the user to input a 9 by 9 sudoku board, complete or incomplete, in the order of left to right, top to bottom and be told if the board is valid meaning that it is solved or can be solved.
* (2) Allows the user to play sudoku with a board that comes with
* (3) Will run a test evaluating runtime on 49151 boards using arc consistency and forward checking with corresponding histograms.
* (4) Runs the MCV test suite and displays resulting graphs

Most constrained value (MCV) was not included in the main testing suite because it is not suitable for boards missing many values as runtime gets exponentially longer