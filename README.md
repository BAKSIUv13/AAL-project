# AAL-project

## Setting up environment

To create python virtual environment:

`python3 -m venv AAL-project-env`

To activate AAL-project-env:

`source AAL-project-env/bin/activate`

To install requirements:

`pip install -r requirements.txt`

## Running program

To get help run:

`python main.py --help`

To run program (mode 1 is the default mode):

`python main.py --string xyxy`

You can specify the file with input data and enable verbose mode too:

`python main.py --file file_name --is_verbose true`

To run program (mode 2):

`python main.py --mode m2 --string_length 21 --number_of_generations 10`

To run program (mode 3) with the brute force comparison:

`python main.py --mode m3 --start_n 10 --stride 10 --number_of_strides 11 --number_of_generations 2`

To run program (mode 3) - without brute force:

`python main.py --mode m3 --is_m3_fast true --start_n 100 --stride 10 --number_of_strides 11 --number_of_generations 2`
