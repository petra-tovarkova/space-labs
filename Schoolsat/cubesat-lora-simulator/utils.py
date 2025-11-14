import numpy as np

def free_space_path_loss(distance, frequency):
    """
    FSPL = 20*log10(distance) + 20*log10(frequency) + 20*log10(4*pi/c)
    distance in meters, frequency in Hz
    returns loss in dB
    """
    c = 3e8
    fspl = 20*np.log10(distance) + 20*np.log10(frequency) + 20*np.log10(4*np.pi/c)
    return fspl

def received_power(tx_power_dbm, path_loss_db, gain_tx=0, gain_rx=0):
    """Calculate received power in dBm"""
    return tx_power_dbm + gain_tx + gain_rx - path_loss_db
