# ann.py

# %% Import Packages
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import tensorflow as tf


# %% Set User Inputs
# csv Information
set_name = 'training-conference_room_T.csv'
pred_var = 'ambient_temperature_occupant_experiences' # Change to column name in .csv

# Hyperparameters
batch_size = 
test_set_percentage = # express as decimal (i.e. 0.2 for 20%)
n_epochs = 
learning_rate = # See https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam for more


# %% Import & Format Data
# Import
unfrmtd_data = # use pd.read_csv to import your data as a pandas dataframe (df). Make sure your data is in the same folder as your input.

# Format (Normalization)

data = 

# Separate Inputs and Target Output
target =  # this will be an array of the measured results. Use df.pop() from pandas
inpt_shape = data.shape[1] # get number of inputs


# %% Build ANN
# Set input_shape = (inpt_shape,) in your first layer.
# You only need to specify the number of neurons in subsequent layers.
# In the last layer, the number of neurons will be 1. This is your output.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, input_shape=(inpt_shape,)),
    # ...
    tf.keras.layers.Dense(1)])
    
model.summary() # Get summary for verification

# %% Train ANN
# Compile ANN
model.compile(optimizer=tf.optimizers.Adam(learning_rate),
            loss=,
            metrics=[])
    
# Train
train_history = model.fit(data.to_numpy(), target.to_numpy(), batch_size=batch_size, # note how we use ___.to_numpy() here. This is formatting the data to a type TensorFlow can use.
                          validation_split=test_set_percentage,
                          epochs=n_epochs)

# Save Results
cd = os.getcwd()
file_list = os.listdir(cd + '\\ANN\\')
n = str(len(file_list) + 1)
model.save(cd + '\\ANN\\ANN_' + n + '.keras')


# %% Plot Training Data
plt.plot(train_history.history['mape'], color='b')
plt.plot(train_history.history['val_mape'], color='r')
plt.title('ANN Training History')
plt.ylabel('Error')
plt.xlabel('Epoch')
plt.legend(['Training: ', 'Validation: '], loc='upper left')

# Save Results
plt.savefig(cd + '\\training_plots\\training_' + n + '.png', dpi=300)


# %% Calculate Error
# Format input
test = tf.convert_to_tensor(data.to_numpy(), dtype=tf.dtypes.float16)

# Predict output
pred = model(test)
pred = pred.numpy() # changes format to something we can work with

# Format target
target_vals = target.to_numpy()
target_vals = np.reshape(target_vals, (target_vals.size, 1))

# Compare output and target
calc_error = # write own equation for error

# Save
x = pd.DataFrame([[n, set_name, batch_size, test_set_percentage, n_epochs,
                   learning_rate, calc_error]],
                 columns=['ANN', 'Training Data', 'Batch Size',
                          'Test Set Percentage', 'Epochs', 'Learning Rate',
                          'Error'])

records = pd.read_csv('ANN_History.csv')

if len(records) == 0:
    records = x

else:
    records = pd.concat([records, x], ignore_index=True)

records.to_csv(cd + '\\ANN_History.csv', index=False)

# %% Plot QQ Chart
# target: the true, measured value for the parameter you are guessing, stored in the csv
# pred: the ANN's predictions.
# Make sure that each value in the arrays match, meaning that the nth element of target 
# corresponds to the same inputs (row of the csv) as the nth value of pred.

# Reverse Normalization
target_rnrm = 
pred_rnrm = 

# Plot data points
qq_plt, ax = plt.subplots()
ax.scatter(target_rnrm, pred_rnrm, marker='.', alpha=0.5, color='#3383FF',
           linewidths=0.1, zorder=1)

# Plot y = x through plot
xmin, xmax, ymin, ymax = ax.axis()

max_pt = max(xmax, ymax) + 1

ax.plot([0, max_pt], [0, max_pt], alpha=1, color='black', linewidth=0.75,
         zorder=2)

# Reset axes's range
pmin = min(xmin, ymin)
pmax = max(xmax, ymax)

ax.set_xlim(pmin, pmax)
ax.set_ylim(pmin, pmax)

# Label
ax.set_title('QQ Plot of ' + pred_var)
if pred_var == 'V':
    ax.set_ylabel(u'ANN Results (m/s)')
    ax.set_xlabel(u'CFD Results (m/s)')
else:
    ax.set_ylabel(u'ANN Results (\u00B0C)')
    ax.set_xlabel(u'CFD Results (\u00B0C)')

qq_plt.savefig(cd + '\\qq_plots\\qq_plot_' + n + '.png', dpi=300)