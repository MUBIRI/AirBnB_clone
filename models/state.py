#!/usr/bin/python3
"""Class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

	def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
