import numpy as np
import mir_eval
import re
import intervals as interval
import testing

# --- Chord Label Parsing ---
# Taken from mir_eval, not available in 0.4 release
def validate_chord_label(chord_label):
    """Test for well-formedness of a chord label.
    Parameters
    ----------
    chord : str
        Chord label to validate.
    """
    # This monster regexp is pulled from the JAMS chord namespace,
    # which is in turn derived from the context-free grammar of
    # Harte et al., 2005.
    pattern = re.compile(r'''^((N|X)|(([A-G](b*|#*))((:(maj|min|dim|aug|1|5|sus2|sus4|maj6|min6|7|maj7|min7|dim7|hdim7|minmaj7|aug7|9|maj9|min9|11|maj11|min11|13|maj13|min13)(\((\*?((b*|#*)([1-9]|1[0-3]?))(,\*?((b*|#*)([1-9]|1[0-3]?)))*)\))?)|(:\((\*?((b*|#*)([1-9]|1[0-3]?))(,\*?((b*|#*)([1-9]|1[0-3]?)))*)\)))?((/((b*|#*)([1-9]|1[0-3]?)))?)?))$''')  # nopep8
    if not pattern.match(chord_label):
        print('Invalid chord label: ''{}'.format(chord_label))
    pass


def label_to_hip(chord_label, intervals=interval.valid_intervals, include_bass=True, include_root=True):
    """Return the hip of a chroma vector

    Parameters
    ----------
    chord_label : str
        chord label

    intervals : list
        list of intervals to compute profiles of

    Returns
    -------
    harmonic interval profile : list 
    """
    validate_chord_label(chord_label)
    root, chroma, bass = mir_eval.chord.encode(chord_label)
    interval_profiles = np.concatenate([interval.interval_profile(i, chroma) for i in intervals])
    bass_onehot = []
    root_onehot = []
    if include_bass:
        bass_onehot = np.eye(13, dtype=int)[np.mod(bass, 13)]
    if include_root:
        root_onehot = np.eye(13, dtype=int)[root]
    hip = np.hstack((root_onehot, interval_profiles, bass_onehot)).astype(int)
    return(hip)


def chroma_to_hip(chroma, intervals=interval.valid_intervals):
    """Return the hip of a chroma vector

    Parameters
    ----------
    chroma : array
        12-dimensional chroma array

    intervals : list
        list of intervals to compute profiles of

    Returns
    -------
    harmonic interval profile : list 
    """
    interval_profiles = np.concatenate([interval.interval_profile(i, chroma) for i in intervals])
    hip = interval_profiles.astype(int)
    return(hip)


def ship(hips):
    """Return a shared harmonic interval profile (ship) from 
    multiple harmonic interval profiles (hip)

    Parameters
    ----------
    hips : list
        list of multiple hip

    norm : list
        norm to normalize the hips by

    Returns
    -------
    ship: list
    """  
    ships = hips.mean(axis=0)
    return(ships)
