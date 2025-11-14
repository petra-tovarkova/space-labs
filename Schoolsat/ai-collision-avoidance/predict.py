import numpy as np
from keras.models import load_model

# nahrání předtrénovaného modelu
model = load_model("collision_model.h5")

# simulovaná data: relativní pozice a rychlost objektů
test_input = np.array([[1000, 200, 5, 0.5]])  # distance_x, distance_y, vel_x, vel_y

# predikce kolize (1 = kolize, 0 = bezpečno)
prediction = model.predict(test_input)
if prediction[0][0] > 0.5:
    print("Collision predicted! Activating avoidance maneuvers.")
else:
    print("Safe trajectory.")
