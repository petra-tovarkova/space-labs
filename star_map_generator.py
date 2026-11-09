# ======================================================
# Space Labs – Live Night Sky Star Map Generator
# Author: Petra Továrková
# Calculates real-time alt/azimuth positions based on location & time.
# ======================================================

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timezone
from astropy.coordinates import EarthLocation, SkyCoord, AltAz
from astropy.time import Time
import astropy.units as u

def generate_live_star_map(lat=49.1905, lon=16.6080):  # Default location: Brno, CZ
    # Catalog of stars with fixed equatorial coordinates (ICRS: RA hours, Dec deg)
    stars = {
        "Sirius": (6.752, -16.716, 120),
        "Canopus": (6.399, -52.715, 90),
        "Alpha Centauri": (14.659, -60.833, 100),
        "Betelgeuse": (5.919, 7.407, 110),
        "Vega": (18.615, 38.783, 95),
        "Polaris": (2.530, 89.264, 80)
    }

    # Observer location & current UTC time
    observer_location = EarthLocation(lat=lat * u.deg, lon=lon * u.deg, height=200 * u.m)
    current_time = Time(datetime.now(timezone.utc))

    # Setup polar plot for local horizon (Zenith at center, horizon at outer edge)
    fig = plt.figure(figsize=(9, 9), facecolor="#0d1117")
    ax = fig.add_subplot(111, polar=True, facecolor="#0d1117")

    visible_stars = 0

    for name, (ra_h, dec_d, size) in stars.items():
        # Define star in ICRS coordinates
        star_coord = SkyCoord(ra=ra_h * u.hourangle, dec=dec_d * u.deg, frame='icrs')
        
        # Transform equatorial to local horizontal coordinates (AltAz)
        altaz_frame = AltAz(obstime=current_time, location=observer_location)
        local_coord = star_coord.transform_to(altaz_frame)

        alt = local_coord.alt.deg
        az = local_coord.az.rad  # Azimuth in radians for polar plot

        # Only plot stars above the horizon (Altitude > 0°)
        if alt > 0:
            visible_stars += 1
            # Polar radius r: 0 at Zenith (90° alt), 90 at horizon (0° alt)
            r = 90.0 - alt
            ax.scatter(az, r, s=size, label=f"{name} ({alt:.1f}°)", alpha=0.9, edgecolors="white", linewidths=0.5)

    # Style polar plot (North = 0°, clockwise azimuth)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 90)
    ax.set_yticklabels([])  # Hide radial labels
    ax.grid(color="#ffffff", alpha=0.15, linestyle="--")

    time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plt.title(f"Live Night Sky Map ({time_str})\nLat: {lat}°, Lon: {lon}° | Visible: {visible_stars}\n", 
              color="#ffffff", fontsize=13, fontweight="bold")

    legend = ax.legend(loc="upper right", bbox_to_anchor=(1.35, 1.1), facecolor="#161b22", edgecolor="#30363d")
    for text in legend.get_texts():
        text.set_color("white")

    print(f"\n✨ Live sky calculated for {time_str} UTC! Visible stars above horizon: {visible_stars}")
    
    output_filename = "star_map.png"
    plt.savefig(output_filename, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"🌌 Saved live render to '{output_filename}'!")

if __name__ == "__main__":
    generate_live_star_map()