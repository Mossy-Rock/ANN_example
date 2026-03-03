# ANN Example
Basic ANN used to allow students without strong programming experince the basics of ANN training using TensorFlow. It includes:

1. ANN_history.csv: A file that contains information about each ANN trained. This provides students with a single table that shows all training parameters and the resulting mean averager percent error (MAPE) of each ANN.
2. ann.py: This is the code that trains the ANN.
3. training-conference_room_T.csv: This contains training data gathered from >3,000 computational fluid dyanmic simulations. "ambient_temperature_occupant_experiences" is the dependent variable.

Before use, the user must create three folders in the same directory as ann.py, with the following names:

1. ANN: This is where the trained ANNs are saved.
2. qq_plots: This is where the Q-Q plots of ANN testing are saved.
3. training_plots: This is where plots of the residual during training are saved.


## Details:
Made using python 3.10
Apache 2.0 License
