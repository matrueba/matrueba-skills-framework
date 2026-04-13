#!/bin/bash
# 
# Manage Documentation Skill - Wrapper Script
# Simplifies running the documentation generation workflow
#
# Usage:
#   ./generate-documentation.sh <project_path> [service_name] [gitlab_link]
#
# Example:
#   ./generate-documentation.sh /path/to/project "My Service" "https://gitlab.com/..."
#

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="${1:-.}"
SERVICE_NAME="${2:-}"
GITLAB_LINK="${3:-}"

# Function to print colored output
print_info() {
    echo -e "${BLUE}ℹ ${NC}$1"
}

print_success() {
    echo -e "${GREEN}✓ ${NC}$1"
}

print_warning() {
    echo -e "${YELLOW}⚠ ${NC}$1"
}

print_error() {
    echo -e "${RED}✗ ${NC}$1"
}

# Function to print usage
usage() {
    cat << EOF
${BLUE}Manage Documentation Skill - Documentation Generation${NC}

${YELLOW}USAGE:${NC}
  $(basename "$0") <project_path> [service_name] [gitlab_link]

${YELLOW}ARGUMENTS:${NC}
  project_path    (required) Path to the project to analyze
  service_name    (optional) Service name (auto-detected if not provided)
  gitlab_link     (optional) GitLab repository link

${YELLOW}EXAMPLES:${NC}
  # Analyze current directory
  $(basename "$0") .

  # Analyze specific directory with service name
  $(basename "$0") /path/to/project "My Microservice"

  # Full example with all info
  $(basename "$0") /path/to/project "Authentication Service" \\
    "https://gitlab.com/myorg/auth-service"

${YELLOW}OUTPUT:${NC}
  Generated documentation will be created in: <project_path>/docs/

${YELLOW}REQUIREMENTS:${NC}
  - Python 3.6 or higher
  - Git installed and configured
  - Project must be a git repository

EOF
    exit 1
}

# Check if help is requested
if [[ "$1" == "-h" || "$1" == "--help" || "$1" == "help" ]]; then
    usage
fi

# Validate project path
if [[ -z "$PROJECT_ROOT" ]] || [[ "$PROJECT_ROOT" == "-"* ]]; then
    print_error "Project path is required"
    usage
fi

if [[ ! -d "$PROJECT_ROOT" ]]; then
    print_error "Project path does not exist: $PROJECT_ROOT"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed"
    exit 1
fi

print_info "Python version: $(python3 --version)"

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed"
    exit 1
fi

# Print configuration
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}DOCUMENTATION GENERATION CONFIGURATION${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
print_info "Project path: $PROJECT_ROOT"
if [[ -n "$SERVICE_NAME" ]]; then
    print_info "Service name: $SERVICE_NAME"
else
    print_info "Service name: (auto-detect)"
fi
if [[ -n "$GITLAB_LINK" ]]; then
    print_info "GitLab link: $GITLAB_LINK"
else
    print_info "GitLab link: (to be filled)"
fi
echo ""

# Build Python command without eval to avoid shell injection issues
PYTHON_CMD=(python3 "$SCRIPT_DIR/scripts/manage_docs.py" "$PROJECT_ROOT")

if [[ -n "$SERVICE_NAME" ]]; then
    PYTHON_CMD+=("$SERVICE_NAME")

    if [[ -n "$GITLAB_LINK" ]]; then
        PYTHON_CMD+=("$GITLAB_LINK")
    fi
fi

# Execute Python script
"${PYTHON_CMD[@]}"

EXIT_CODE=$?

if [[ $EXIT_CODE -eq 0 ]]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    print_success "Documentation generation completed successfully!"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    print_info "Documentation location: $PROJECT_ROOT/docs/"
    echo ""
    print_warning "IMPORTANT: Review and complete the generated documentation"
    print_warning "See docs/main.md and other generated files for details"
    echo ""
else
    echo ""
    print_error "Documentation generation failed with exit code: $EXIT_CODE"
    exit $EXIT_CODE
fi
