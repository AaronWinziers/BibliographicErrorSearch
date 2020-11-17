# Error Finder

This script can be used to find the errors in the raw bibliographic data. 

Not all errors in tagging are caused by the issue explained in the [Tagging Fixer](https://github.com/AaronWinziers/TaggingFixer), and some can be caused by errors in the raw data.

This script makes finding these errors much simpler by counting t enumber of tags in each step of the tagging process for each document.

## Example output 
Below is an example of the output for a single document. The columns represent each step of the tagging process (entry | det | res | au | ae | ae_se).

The given example os a file which shows no irregularities. The number of tags should only increase and most tags should only appear a single time per document.

    ======
    64.11:
    ======
    1 1 1 1 1 1 	entry
    1 1 1 1 1 1 	ti
    0 0 0 0 0 0 	au
    1 1 1 1 1 1 	det
    1 1 1 1 1 1 	bib
    0 0 0 0 0 0 	ex
    0 0 0 0 0 0 	res
    0 0 0 0 0 0 	tr
    1 1 1 1 1 1 	ae
    0 1 1 1 1 1 	pl
    0 1 1 1 1 1 	pb
    0 1 1 1 1 1 	y
    0 1 1 1 1 1 	f
    0 1 1 1 1 1 	p
    0 0 0 0 0 0 	a
    0 0 0 0 0 0 	trd
    0 0 0 0 0 0 	ed
    
The following example shows a document with obvious issues:

    ======
    52.12:
    ======
    1 1 1 1 1 1 	entry
    2 2 2 2 2 2 	ti
    1 1 1 1 1 1 	au
    1 1 1 1 1 1 	det
    1 1 1 1 1 1 	bib
    1 1 1 1 1 1 	ex
    1 1 1 1 1 1 	res
    0 0 0 0 0 0 	tr
    1 1 1 1 1 1 	ae
    0 1 1 1 1 1 	pl
    0 0 0 0 0 0 	pb
    0 1 1 1 1 1 	y
    0 1 1 1 1 1 	f
    0 1 1 1 1 1 	p
    0 0 0 1 1 1 	a
    0 0 0 0 0 0 	trd
    0 0 0 0 0 0 	ed
    
The data for this entry should be checked, because it is irregular for two <ti> (title) tags to belong to a single document. and as can be seen below, the raw data obviously encapsulates two separate documents and should be amended.

Additionally, the script outputs a list of IDs that is incorrectly formatted, as well as a list of IDs that are doubled in the data. These will always be errors that should be addressed.

## Usage

To execute the script, Python 3 and pip3 are required.

In order to run the script, either download the ZIP version of this repository and unpack it or clone it using the following:

    git clone https://github.com/AaronWinziers/DataErrorFinder.git
    
Before executing, the location of the files that need to be checked should be amended in line 4 of the script.
    
Navigate into the folder containing the code, and execute the following in order to install the required packages:

    pip3 install -r requirements.txt

Then, enter the following to execute the script:

    python3 main.py