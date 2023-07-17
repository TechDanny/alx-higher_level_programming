#!/usr/bin/python3
"""
create a class
"""


import json
import locale


class Base:
    """
    define a private class attribute
    """
    __nb_objects = 0

    """
    define a class constructor
    """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation
        of list dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list) or not all(type(n) == dict
           for n in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list objs to a file
        """
        fn = cls.__name__ + ".json"
        with open(fn, "w", encoding=locale.getpreferredencoding()) as f:
            if list_objs is None:
                f.write("[]")
            else:
                my_list = [n.to_dictionary() for n in list_objs]
                f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
        return the list of the JSON string representation
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_update = cls(1, 1)
            else:
                new_update = cls(1)
            new_update.update(**dictionary)
            return new_update

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        fn = str(cls.__name__) + ".json"
        try:
            with open(fn, "r", encoding=locale.getpreferredencoding()) as f:
                my_list = Base.from_json_string(f.read())
                return [cls.create(**n) for n in my_list]
        except IOError:
            return []
