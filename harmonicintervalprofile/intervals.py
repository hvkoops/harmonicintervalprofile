import numpy as np


valid_intervals     = [1, 3, 5, 7, 8, 10]
valid_intervals_str = ['second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']


class InvalidChromaException(Exception):
    r'''Exception class for suspect / invalid chroma'''
    def __init__(self, message='', chroma=None):
        self.message = message
        self.chroma = chroma
        self.name = self.__class__.__name__
        super(InvalidChromaException, self).__init__(message)


class InvalidIntervalException(Exception):
    r'''Exception class for suspect / invalid interval'''
    def __init__(self, message='', interval=None):
        self.message = message
        self.interval = interval
        self.name = self.__class__.__name__
        super(InvalidIntervalException, self).__init__(message)


def validate_chroma(chroma):
    """Test for well-formedness of chroma.
    Parameters
    ----------
    chroma : array
        Chroma array to validate
    """
    uniquesum = np.unique(chroma).sum()
    if not (uniquesum == 1) and (chroma.shape[0] == 12):
        raise InvalidChordException('Invalid chroma: ''{}'.format(chroma))
    pass


def validate_interval(interval):
    """Test for interval correctness.
    Parameters
    ----------
    interval : int
        integer representation of interval to validate
    """
    if not (interval in valid_intervals):
        raise InvalidChordException('Invalid interval: ''{}'.format(interval))
    pass    


# The second, third, sixth, and seventh intervals (and compound intervals
# based on them) may be either major or minor.
def majmin_intervals():
    """Return the major/minor/both/none options of an interval

    Parameters
    ----------
    none

    Returns
    -------
    qualities : array
        one of:
        [0,1]: Major 
        [1,0]: Minor 
        [1,1]: Both major and minor 
        [0,0]: None
    """
    qualities = np.array([[0, 1],[1, 0],[1, 1],[0, 0]])
    return(qualities)    


# perfect intervals (including the unison, perfect fourth and octave)
def perfect_intervals():
    """Return the perfect/none options of an interval

    Parameters
    ----------
    none

    Returns
    -------
    qualities : array
        one of:
        [1]: Perfect
        [0]: None/absent
    """
    qualities = np.array([[1],[0]])
    return(qualities)    


def interval_profile(interval, chroma):
    """Return the n-interval profile of a chroma vector

    Parameters
    ----------
    interval : int
        interval to compute profile of

    chroma : array
        12-dimensional chroma array to validate

    Returns
    -------
    profile : array
        in case of "major/minor" interval (second, third, 
            sixth, and seventh interval):
        [1,0,0,0]: Major second
        [0,1,0,0]: Minor second
        [0,0,1,0]: Both major and minor seconds
        [0,0,0,1]: Absent seconds

    or in case of "perfect" intervals (fourth or fifth):
        [1,0]: Perfect
        [0,1]: None/absent    
    """
    validate_chroma(chroma)
    validate_interval(interval)
    if interval in [1, 3, 8, 10]:
        qualities = majmin_intervals()
        interval_range = 2
    if interval in [5, 7]:
        qualities = perfect_intervals()
        interval_range = 1
    profile_matches = np.all(chroma[interval:interval+interval_range] == qualities, axis=1)
    profile = np.array(profile_matches, dtype=int)
    return(profile)  

