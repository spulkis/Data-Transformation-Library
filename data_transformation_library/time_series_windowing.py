import numpy as np

def window1d(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
    """
    Extracts overlapping or non-overlapping windows from a 1D array based on the specified size, shift, and stride.

    Parameters:
    ----------
    input_array : list | np.ndarray
        A list or 1D NumPy array of real numbers from which to extract windows.
    size : int
        A positive integer specifying the length of each window.
    shift : int, optional
        A positive integer specifying the shift (step size) between different windows. Default is 1.
    stride : int, optional
        A positive integer specifying the stride (step size) within each window. Default is 1.

    Returns:
    -------
    list[list | np.ndarray]
        A list of windows, where each window is represented as a list or 1D NumPy array of real numbers,
        matching the input type of `input_array`.

    Raises:
    ------
    ValueError
        If `size` is less than or equal to 0, or if `shift` or `stride` are less than or equal to 0.
    TypeError
        If `input_array` is not a list or NumPy ndarray, or if `size`, `shift`, or `stride` are not integers.

    Example:
    -------
    >>> input_array = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    >>> size = 3
    >>> shift = 2
    >>> stride = 1
    >>> window1d(input_array, size, shift, stride)
    [[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [5.0, 6.0]]
    >>> input_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    >>> window1d(input_array, size, shift, stride)
    [array([1., 2., 3.]), array([3., 4., 5.]), array([5., 6.])]
    """

    # Type, Value checks
    if not isinstance(input_array, (list, np.ndarray)):
        raise TypeError("input_array must be a list or a 1D NumPy array")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    if not isinstance(shift, int) or shift <= 0:
        raise ValueError("Shift must be a positive integer")
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("Stride must be a positive integer")
    
    # Initialize an empty list to store the windows
    windows = []
    
    # Process input if it is a list
    if isinstance(input_array, list):
        for i in range(0, len(input_array) - size + 1, shift):
            window = input_array[i:i + size:stride]
            windows.append(window)
    # Process input if it is a NumPy array
    elif isinstance(input_array, np.ndarray):
        for i in range(0, input_array.size - size + 1, shift):
            window = input_array[i:i + size:stride]
            windows.append(window)
    return windows
