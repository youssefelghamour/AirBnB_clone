# 0x00. AirBnB clone - The console

## Description
This project is an implementation of the first step towards building an AirBnB clone. The main focus is on creating a command interpreter to manage AirBnB objects. The project involves the use of Python, Object-Oriented Programming (OOP), and concepts like JSON serialization, deserialization, and unit testing.

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

  ##### `base_model.py`
  - The base class for all the models.

  #### `engine/`
  - Directory containing storage classes for the JSON serialization and deserialization.

    ##### `file_storage.py`
     - Serializes instances to a JSON file and deserializes JSON file to instances

#### `tests/`
- Directory for unit tests.

## Authors
* **Mahmoud Hammam** - [MahmoudHammam0](https://github.com/MahmoudHammam0)
* **Youssef El Ghamour** - [youssefelghamour](https://github.com/youssefelghamour)
