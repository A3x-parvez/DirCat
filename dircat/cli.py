import argparse
import sys
import os
from dircat.core import create_structure
from dircat.utils import load_input
from dircat.ui import show_home
from rich.live import Live
from dircat.ui import show_loader, show_success

VERSION = "0.1.0"
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


# -----------------------------
# Template Utilities
# -----------------------------
def list_templates():
    files = os.listdir(TEMPLATE_DIR)
    templates = [f.replace(".json", "") for f in files if f.endswith(".json")]

    print("\n📦 Available Templates:\n")
    for t in templates:
        print(f"  - {t}")
    print("")


def load_template(name):
    path = os.path.join(TEMPLATE_DIR, f"{name}.json")

    if not os.path.exists(path):
        print(f"❌ Template '{name}' not found")
        sys.exit(1)

    return load_input(path)


# -----------------------------
# Commands
# -----------------------------
def handle_create(args):
    if args.template:
        config = load_template(args.template)

    elif args.input:
        try:
            config = load_input(args.input)
        except Exception as e:
            print(f"❌ Error parsing input: {e}")
            sys.exit(1)
    else:
        print("❌ Provide input (JSON/TXT/tree) or use --template")
        sys.exit(1)

    base_path = "." if args.here else os.getcwd()

    # create_structure(
    #     config,
    #     base_path=base_path,
    #     force=args.force,
    #     dry_run=args.dry_run,
    #     verbose=not args.quiet
    # )


    if args.dry_run:
        create_structure(
            config,
            base_path=base_path,
            force=args.force,
            dry_run=True,
            verbose=not args.quiet
        )
    else:
        loader = show_loader()

        with Live(loader, refresh_per_second=12):
            create_structure(
                config,
                base_path=base_path,
                force=args.force,
                dry_run=False,
                verbose=False
            )

        if not args.quiet:
            show_success()


def handle_template(args):
    if args.list:
        list_templates()
    else:
        print("❌ Use --list to see available templates")


def handle_version(_):
    print(f"DirCat version {VERSION}")


# -----------------------------
# Smart Command Injection
# -----------------------------
def auto_inject_create():
    """
    Allow:
        dircat file.txt
        dircat file.json
        dircat "{json}"
        dircat help
    """
    if len(sys.argv) > 1:
        first = sys.argv[1]

        # 🔥 Handle "help" manually
        if first in ["help", "h"]:
            from dircat.ui import show_home
            show_home()
            sys.exit(0)

        valid_commands = {"create", "template", "version", "-h", "--help"}

        # If first arg is NOT a command → assume create
        if first not in valid_commands:
            sys.argv.insert(1, "create")


# -----------------------------
# Main CLI
# -----------------------------
def main():
    # Show homepage if no args
    if len(sys.argv) == 1:
        show_home()
        sys.exit(0)

    # 🔥 Auto-fix command
    auto_inject_create()

    parser = argparse.ArgumentParser(
        prog="dircat",
        description="DirCat 🐱 - Instant project structure generator",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command")

    # -----------------------------
    # CREATE COMMAND
    # -----------------------------
    create_parser = subparsers.add_parser(
        "create",
        help="Create project structure from JSON, TXT, tree, or raw input"
    )

    create_parser.add_argument(
        "input",
        nargs="?",
        help="Path or raw input (JSON/TXT/tree)"
    )
    create_parser.add_argument("--template", help="Use built-in template")
    create_parser.add_argument("--dry-run", action="store_true", help="Preview only")
    create_parser.add_argument("--force", action="store_true", help="Overwrite files")
    create_parser.add_argument("--here", action="store_true", help="Use current directory")
    create_parser.add_argument("--quiet", action="store_true", help="Silent mode")

    create_parser.set_defaults(func=handle_create)

    # -----------------------------
    # TEMPLATE COMMAND
    # -----------------------------
    template_parser = subparsers.add_parser(
        "template",
        help="Manage templates"
    )

    template_parser.add_argument("--list", action="store_true", help="List templates")
    template_parser.set_defaults(func=handle_template)

    # -----------------------------
    # VERSION COMMAND
    # -----------------------------
    version_parser = subparsers.add_parser(
        "version",
        help="Show version"
    )

    version_parser.set_defaults(func=handle_version)

    # -----------------------------
    # PARSE + EXECUTE
    # -----------------------------
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        show_home()


if __name__ == "__main__":
    main()