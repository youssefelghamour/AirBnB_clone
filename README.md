# 0x01. AirBnB clone - Web static

## Description
This project is an implementation of the first step towards building an AirBnB clone. The main focus is on creating a command interpreter to manage AirBnB objects. The back-end work involves the use of Python, Object-Oriented Programming (OOP), and concepts like JSON serialization, deserialization, and unit testing.

Additionally, the project now includes the Web static component, involving front-end development. The goal is to build simple HTML static pages and apply CSS styling, creating a design prototype for AirBnB objects. The project encompasses concepts such as HTML and CSS.

## Command Interpreter
The command interpreter allows users to interact with the AirBnB objects by performing various operations, including creating new objects, retrieving objects from files or databases, updating attributes, and more.

## How to start it:
* Clone this repository: `git clone "https://github.com/MahmoudHammam0/AirBnB_clone.git"`
* Access the AirBnb directory: `cd AirBnB_clone`
* Run hbnb (interactively): `./console` and enter command
* Run hbnb (non-interactively): `echo "<command>" | ./console.py`

### How to use it in:
#### Interactive mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Files and Directories
##### `console.py`
- Entry point for the command interpreter.
- Commands supported include EOF, quit, create, destroy, show, all, and update.

#### `models/`
- Directory containing classes for the project.

  ##### `base_model.py` - The base class for all the models:
  ##### `amenity.py` - Amenity class that inherits from BaseModel.
  ##### `city.py` - City class that inherits from BaseModel.
  ##### `place.py` - Place class that inherits from BaseModel.
  ##### `review.py` - Review class that inherits from BaseModel.
  ##### `state.py` - State class that inherits from BaseModel.
  ##### `user.py` - User class that inherits from BaseModel.

  #### `engine/`
  - Directory containing storage classes for the JSON serialization and deserialization.

    ##### `file_storage.py` - Serializes instances to a JSON file and deserializes JSON file to instances

#### `tests/`
- Directory for unit tests.

  ##### `test_models/`
  - Directory containting tests for all the classes/models:

    ##### `test_amenity.py` - unittest for the Amenity class.
    ##### `test_base_model.py` - unittest for the BaseModel class.
    ##### `test_city.py` - unittest for the city class.
    ##### `test_place.py` - unittest for the Place class.
    ##### `test_review.py` - unittest for the Review class.
    ##### `test_state.py` - unittest for the State class.
    ##### `test_user.py` - unittest for the User class.

    #### `test_engine/`
    - Directory containing for the storage class.

      ##### `test_file_storage.py` - unittest for the FileStorage class.

## Authors
* **Mahmoud Hammam** - [MahmoudHammam0](https://github.com/MahmoudHammam0)
* **Youssef El Ghamour** - [youssefelghamour](https://github.com/youssefelghamour)
