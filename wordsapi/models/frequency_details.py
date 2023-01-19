# -*- coding: utf-8 -*-

"""
wordsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from wordsapi.api_helper import APIHelper


class FrequencyDetails(object):

    """Implementation of the 'FrequencyDetails' model.

    This model contains frequency details of a specific word.

    Attributes:
        zipf (float): Explains the zipf score.
        per_million (float): Explains the perMillion score.
        diversity (float): Explains the diversity score.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "zipf": 'zipf',
        "per_million": 'perMillion',
        "diversity": 'diversity'
    }

    _optionals = [
        'zipf',
        'per_million',
        'diversity',
    ]

    _nullables = [
        'zipf',
        'per_million',
        'diversity',
    ]

    def __init__(self,
                 zipf=APIHelper.SKIP,
                 per_million=APIHelper.SKIP,
                 diversity=APIHelper.SKIP):
        """Constructor for the FrequencyDetails class"""

        # Initialize members of the class
        if zipf is not APIHelper.SKIP:
            self.zipf = zipf 
        if per_million is not APIHelper.SKIP:
            self.per_million = per_million 
        if diversity is not APIHelper.SKIP:
            self.diversity = diversity 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        zipf = dictionary.get("zipf") if "zipf" in dictionary.keys() else APIHelper.SKIP
        per_million = dictionary.get("perMillion") if "perMillion" in dictionary.keys() else APIHelper.SKIP
        diversity = dictionary.get("diversity") if "diversity" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(zipf,
                   per_million,
                   diversity)