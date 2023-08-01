# Stroop Task Experiment with results 

A python program to run the stroop task experiment, with visualized results afterwards


## Why should I use this project ?

It makes it easy to experience the stroop task and gives valuable feedback to the user regarding speed and accuracy


## Setup

You need `python>3.11` to run this program.

The project includes a requirements.txt with all the necessary installations.
To install all of them, you can run:

```
pip install -r requirements.txt
``` 

If you are using Mac, instead run:

```
pip3 install -r requirements.txt
``` 


## How to run?

You can run the script from the command-line using
```
python stroop_main.py
```

If you are using Mac, instead run:
```
python3 stroop_main.py
```

Once you ran it, a window will display the experiment description and rules.
If you are ready, press the "Start" button.
After that, the experiment will begin.
As soon, as you finished the last trial (default: 30, can be changed by the developers by chaging the 'limit' variable), another screen will appear.
You can restart the experiment by clicking on the 'Try again' button or have a look at the visualization of your data by pressing 'Show results'.
After that you can exit the program by simply clicking on the 'x' button.

## Included files

Readme file: 'README.md' -> expaines programm + usage
Python files: 'make_interface.py', 'plot_data.py' and 'stroop_main.py' -> main part of the program
Text file: 'requirements.txt' -> containing all the necesarry installations
Data file: 'combined.csv' -> including trial data of multiple people doing the stroop task. Please make sure not to delete this file as it provides the data which is compared to yours!

## How to cite this project?

You are very welcome to just share this project with whoever might enjoy it 
