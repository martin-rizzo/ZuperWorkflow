#!/usr/bin/env bash
# File    : scripts/print_slice.sh
# Purpose : Wrapper for `print_slice.py`
# Author  : Martin Rizzo | <martinrizzo@gmail.com>
# Date    : Oct 30, 2026
# Repo    : https://github.com/martin-rizzo/ZuperWorkflows
# License : CC0 1.0 Universal
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                               Zuper Workflows
#A pair of workflows for easily generating high-quality images with Z-Image Turbo.
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
[[ -f LICENSE && -d src ]] && IN_PROJECT_ROOT=true
SCRIPTS_DIR='scripts'

# ANSI escape codes for colored terminal output
RED='\e[91m'
GREEN='\e[92m'
YELLOW='\e[93m'
CYAN='\e[96m'
NC='\e[0m'

# Displays a formatted message to standard error.
#
# Usage: message [format] [message...]
#
# Arguments:
#   format    Optional. Specifies the message style. Supported values:
#               check  - Displays a checkmark prefix and closes the line.
#               wait   - Displays a waiting asterisk prefix with ellipsis.
#               info   - Displays an info icon prefix.
#             If omitted, defaults to a standard arrow prefix.
#   message   Optional. The text to display.
#             If both format and message are empty, prints a blank line.
#
# Output:
#   Writes the formatted message to stderr.
#
# Examples:
#   message info  "Using default settings"
#   message check "Build successful"
#   message "Hello, world!"
#
message() {
    local format=$1
    if [[ -z "$format" && -z "$2" ]]; then
        echo >&2
        return
    fi
    local prefix="  ${GREEN}>${NC}"
    local suffix=""
    case "$format" in
        info ) prefix="  ${CYAN}\xE2\x93\x98 "       ; suffix="${NC}"    ; shift ;;
        check) prefix="  ${GREEN}\xE2\x9C\x94${NC} " ; suffix="${NC}"    ; shift ;;
        wait ) prefix="  ${YELLOW}* "                ; suffix="...${NC}" ; shift ;;
    esac
    echo -e -n "$prefix" >&2
    echo    -n "$@"      >&2
    echo    -e "$suffix" >&2
}


# Displays an error message to standard error.
#
# Usage: error [message]
#
# Arguments:
#   message   Optional. The text to display.
#             If omitted, prints just the error label.
#
# Output:
#   Writes the formatted error message to stderr.
#
error() {
    local message=$1
    echo
    echo -e "${CYAN}[${RED}ERROR${CYAN}]${NC} $message" >&2
}


#===========================================================================#
#////////////////////////////////// MAIN ///////////////////////////////////#
#===========================================================================#

# This script is designed to always be called from the project root
# directory, so that generated workflows are placed there.
# Validate this and display an error message if not in the correct directory.
if [[ ! "${IN_PROJECT_ROOT}" ]]; then
    error "Not in the project root directory."
    message info "Please run '${SCRIPTS_DIR}/print_slice.sh' from the project root directory."
    exit 1
fi

python "${SCRIPTS_DIR}/print_slice.py" src/STYLES.sty.txt "$1"
