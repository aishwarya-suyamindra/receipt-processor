
import uuid

def count_alphanumeric_characters(string: str) -> int:
    """
    Helper function to count the number alphanumeric characters in the given string.

    Parameters:
    -----------
    string : str
        The string to retrieve the alphanumeric characters for

    Returns:
    --------
    int
        The number of alphanumeric characters in the given string
    """
    return len([ch for ch in string if ch.isalnum()])

def generate_id() -> str:
    """
    Helper function that uses the UUID library to generate a unqiue ID.

    Returns:
    --------
    str
        A string representing a unique UUID.
    """
    return str(uuid.uuid4())