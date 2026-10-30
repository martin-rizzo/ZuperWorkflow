"""
  File    : filter_segment.py
  Purpose : Filters text lines to extract specific segments based on separators.
  Author  : Martin Rizzo | <martinrizzo@gmail.com>
  Date    : Oct 30, 2026
  Repo    : https://github.com/martin-rizzo/ZuperWorkflow
  License : Unlicense
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                               Zuper Workflow
A pair of workflows for easily generating high-quality images with Z-Image Turbo.
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
"""
import argparse
import os
import sys
type TextLines = list[str]

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

def is_separator(line: str, char: str) -> bool:
    """
    Checks if a line is a valid separator.

    A line is considered a separator if it consists entirely of the
    specified character and has a length of at least 6 characters.

    Args:
        line: The text line to evaluate.
        char: The character that must compose the separator line.

    Returns:
        True if the line is a valid separator, False otherwise.
    """
    return len(line) >= 6 and all(c == char for c in line)


def split_segments(text_lines: TextLines) -> list[TextLines]:
    """
    Splits a list of text lines into segments based on '-' separator lines.

    The function iterates through the provided lines and groups them into
    separate segments. A line consisting entirely of '-' characters (with
    a length of at least 6) acts as a segment delimiter, starting a new
    segment.

    Args:
        text_lines: A list of strings representing the lines of text to be split.

    Returns:
        A list of lists of strings, where each inner list represents a segment.
    """
    segments: list[TextLines] = [[]]
    segment_idx = 0

    for line in text_lines:
        if is_separator(line, '-'):
            segment_idx += 1
            if segment_idx >= len(segments):
                segments.append([])
        else:
            segments[segment_idx].append(line)

    return segments


#------------------------------ MAIN FUNCTION ------------------------------#


def filter_segment(text_lines       : TextLines,
                   segment_to_filter: int,
                   *,
                   replace_hashes   : bool
                   ) -> TextLines:
    """
    Filters text lines to extract a specific segment.

    Scans through the provided lines, identifying a block of text enclosed
    by separator lines ('------' to start, '======' to end). The start and
    end separators are consumed and not included in the output. Within this
    block, multiple segments may be separated by '-' lines. The function
    extracts the lines belonging to the segment at the given index (1-based)
    and returns them as a list of strings. Lines outside the main block
    are also preserved in the output.

    Args:
        text_lines:        A list of strings representing the input text lines.
        segment_to_filter: The 1-based index of the segment to extract.
        replace_hashes:    If True, replaces leading '###' with '>>>' in the output.

    Returns:
        A list of strings containing the filtered lines, including both
        the selected segment's content and any lines outside the main block.
    """
    result         : TextLines = []
    segmented_lines: TextLines = []
    in_segments    : bool      = False
    segment_idx    : int       = segment_to_filter - 1

    for line in text_lines:

        # if a simple separator is found, start the segmentation process
        if is_separator(line, '-') and not in_segments:
            in_segments = True
            segmented_lines = []
            continue

        # if a double separator ("=") is found, end the segmentation process
        if is_separator(line, '=') and in_segments:
            in_segments = False

            # store only the content of the user-selected segment
            segments = split_segments(segmented_lines)
            if segments and 0 <= segment_idx < len(segments):
                result.extend(segments[segment_idx])
            continue

        # if it's a regular text line, append it to the corresponding list
        if in_segments: segmented_lines.append(line)
        else:           result.append(line)


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
        description="Separates the content of a text file by filtering only the segments between '------' that match the chosen segment index.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("filename", help="Input file name")
    parser.add_argument("index", type=int, help="Segment index to filter (starting from 1)")
    args = parser.parse_args(args=parent_args)

    # verify that the input file exists
    if not os.path.exists(args.filename):
        error(f"File '{args.filename}' not found.")
        sys.exit(1)

    # read all lines from the input file
    with open(args.filename, 'r') as f:
        lines = f.read().splitlines()

    # filter lines based on the specified segment index
    filtered_lines = filter_segment(lines, args.index, replace_hashes=True);
    print("\n".join(filtered_lines))


if __name__ == "__main__":
    main()
