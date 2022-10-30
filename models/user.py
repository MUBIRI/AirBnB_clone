#!/usr/bin/python3
"""Class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

	def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
