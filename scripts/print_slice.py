"""
  File    : print_slice.py
  Purpose : Prints a specific slice from a text file based on markers.
  Author  : Martin Rizzo | <martinrizzo@gmail.com>
  Date    : Oct 30, 2026
  Repo    : https://github.com/martin-rizzo/ZuperWorkflows
  License : Unlicense
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                               Zuper Workflows
A pair of workflows for easily generating high-quality images with Z-Image Turbo.
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
"""
import argparse
import os
import sys
type TextLines = list[str]
SLICE_MODE_BEGIN  = "{-----"  #< Marks the beginning of the slicing mode
SLICE_MODE_END    = "-----}"  #< Marks the end of the slicing mode
NEXT_SLICE_MARKER = "------"  #< Indicates the start of the next slice
COMMENT_BEGIN     = "{-----COMMENT"
COMMENT_END       = "-----}"


# ANSI escape codes for colored terminal output
RED      = '\033[91m'
DKRED    = '\033[31m'
YELLOW   = '\033[93m'
DKYELLOW = '\033[33m'
GREEN    = '\033[92m'
CYAN     = '\033[96m'
DKGRAY   = '\033[90m'
RESET    = '\033[0m'


#----------------------------- ERROR MESSAGES ------------------------------#

def disable_colors():
    global RED, DKRED, YELLOW, DKYELLOW, GREEN, CYAN, DKGRAY, RESET
    RED, DKRED, YELLOW, DKYELLOW, GREEN, CYAN, DKGRAY, RESET = "", "", "", "", "", "", "", ""


def info(message: str, padding: int = 0, file=sys.stderr) -> None:
    """Displays an informational message to the error stream.
    """
    print(f"{' '*padding}{CYAN}\u24d8 {message}{RESET}", file=file)


def error(message: str, *info_messages: str, padding: int = 0, file=sys.stderr) -> None:
    """Displays an error message to the standard error stream.
    """
    print(f"{' '*padding}{DKRED}[{RED}ERROR!{DKRED}]{DKYELLOW} {message}{RESET}", file=file)
    for info_message in info_messages:
        if info_message:
            info(info_message, padding=padding, file=file)


#---------------------------- HELPER FUNCTIONS -----------------------------#

def cut_into_slices(text_lines: TextLines) -> list[TextLines]:
    """
    Splits a list of text lines into multiple slices based on separator lines.

    Iterates through the provided lines and groups them into separate slices.
    A line consisting entirely of 6 '-' characters acts as a slice delimiter,
    starting a new slice. Lines before the first separator are grouped into
    the first slice.

    Args:
        text_lines: A list of strings representing the lines of text to be split.

    Returns:
        A list of lists of strings, where each inner list represents a slice.
    """
    slices: list[TextLines] = [[]]
    slice_idx = 0

    for line in text_lines:
        if line == NEXT_SLICE_MARKER:
            slice_idx += 1
            if slice_idx >= len(slices):
                slices.append([])
        else:
            slices[slice_idx].append(line)

    return slices


#------------------------------ MAIN FUNCTION ------------------------------#


def filter_slices(text_lines       : TextLines,
                  slice_to_filter  : int,
                  *,
                  replace_hashes   : bool
                  ) -> TextLines:
    """
    Filters text lines to extract specific slices based on markers.

    This function processes a list of text lines, identifying blocks of text
    enclosed by `SLICE_MODE_BEGIN` and `SLICE_MODE_END` markers. Inside each
    block, lines are divided into slices using `NEXT_SLICE_MARKER` as a
    delimiter. The function extracts the slice at the `slice_to_filter` index
    (1-based) from *each* identified block and combines them with any lines
    that appear outside the blocks.

    Additionally, if `replace_hashes` is True, any line starting with "###"
    within the extracted content will have its leading "###" replaced with
    ">>>".

    Args:
        text_lines:      A list of strings representing the input text lines.
        slice_to_filter: The 1-based index of the slice to extract from each
                         identified block.
        replace_hashes:  If True, replaces leading ``###`` with ``>>>``.
                         Defaults to False.

    Returns:
        A list of strings containing the filtered lines. This includes the
        content of the selected slices from each block and any lines that
        were outside the marker blocks.
    """
    result      : TextLines = []
    sliced_lines: TextLines = []
    in_slices   : bool      = False
    in_comment  : bool      = False
    slice_idx   : int       = slice_to_filter - 1

    for line in text_lines:

        # start of comment block
        if line == COMMENT_BEGIN:
            in_comment = True
            continue

        # end of comment block
        if line == COMMENT_END and in_comment:
            in_comment = False
            continue

        # start the slicing process when the beginning marker is encountered
        if line == SLICE_MODE_BEGIN and not in_comment:
            if not in_slices:
                in_slices = True
                sliced_lines = []
                continue

        # end the slicing process when the ending marker is encountered
        if line == SLICE_MODE_END and not in_comment:
            if in_slices:
                in_slices = False

                # store only the content of the user-selected slice
                slices = cut_into_slices(sliced_lines)
                if slices and 0 <= slice_idx < len(slices):
                    result.extend(slices[slice_idx])
                continue

        # append lines to the appropriate list based on whether we are
        # inside the slice block (ignoring lines inside comments)
        if not in_comment:
            if in_slices: sliced_lines.append(line)
            else:         result.append(line)


    if replace_hashes:
        fixed_result: TextLines = []
        for line in result:
            if line.startswith("###"): fixed_result.append(">>>" + line[3:])
            else:                      fixed_result.append(line)
        result = fixed_result

    return result



#===========================================================================#
#////////////////////////////////// MAIN ///////////////////////////////////#
#===========================================================================#

def main(parent_args=None, parent_script=None):
    """
    Main entry point for the script.
    Args:
        args          (optional): List of arguments to parse. Default is None, which will use the command line arguments.
        parent_script (optional): The name of the calling script if any. Used for customizing help output.
    """
    prog = None
    if parent_script:
        prog = parent_script + " " + os.path.basename(__file__).split('.')[0]

    # set up argument parser for the script
    parser = argparse.ArgumentParser(
        prog=prog,
        description="Separates the content of a text file by printing only the slices that match the chosen index.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("filename", help="Input file name")
    parser.add_argument("index", type=int, help="Index of the slice to print (starting from 1)")
    args = parser.parse_args(args=parent_args)

    # verify that the input file exists
    if not os.path.exists(args.filename):
        error(f"File '{args.filename}' not found.")
        sys.exit(1)

    # read all lines from the input file
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()

    # filter lines based on the specified slice index
    filtered_lines = filter_slices(lines, args.index, replace_hashes=True);
    print("\n".join(filtered_lines))


if __name__ == "__main__":
    main()
