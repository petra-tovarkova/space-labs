import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def generate_star_map():
    # Example data for stars (just a few for demonstration)
    stars = {
        "Sirius": (6.752, -16.716),  # (RA, Dec) in degrees
        "Canopus": (6.399, -52.715),
        "Alpha Centauri": (14.000, -60.833),
        "Betelgeuse": (5.919, 7.407)
    }

    fig, ax = plt.subplots(figsize=(8, 8))
    for star, coordinates in stars.items():
        ra, dec = coordinates
        ax.scatter(ra, dec, label=star)

    ax.set_xlabel("Right Ascension (RA)")
    ax.set_ylabel("Declination (Dec)")
    ax.set_title("Star Map")
    ax.legend()
    plt.show()

generate_star_map()
