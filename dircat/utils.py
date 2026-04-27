# import json
# import re
# import os

# def is_tree_format(text):
#     return "├──" in text or "└──" in text


# def extract_json(text):
#     """
#     Extract JSON from messy AI / txt content
#     """
#     match = re.search(r"\{.*\}", text, re.DOTALL)
#     if match:
#         return match.group()
#     return text


# def load_input(input_arg):
#     """
#     Supports:
#     - .json, .txt, ANY file
#     - raw JSON string
#     - messy GPT output
#     """

#     # Case 1: It's a file (any extension)
#     if os.path.exists(input_arg):
#         with open(input_arg, "r", encoding="utf-8") as f:
#             content = f.read()
#     else:
#         # Case 2: direct string input
#         content = input_arg

#     # Clean markdown if pasted from AI
#     content = content.replace("```json", "").replace("```", "")

#     # Extract JSON part
#     content = extract_json(content)

#     try:
#         return json.loads(content)
#     except Exception as e:
#         raise ValueError(f"Invalid JSON format: {e}")
    


# def parse_tree_structure(text):
#     folders = []
#     files = []

#     lines = text.splitlines()
#     stack = []

#     root = None

#     for line in lines:
#         if not line.strip():
#             continue

#         # Clean symbols
#         clean = line.replace("│", "").replace("├──", "").replace("└──", "").strip()

#         level = (len(line) - len(line.lstrip())) // 4

#         is_folder = clean.endswith("/")
#         name = clean.rstrip("/")

#         if level == 0:
#             root = name
#             stack = [(level, name)]
#             continue

#         while stack and stack[-1][0] >= level:
#             stack.pop()

#         parent = stack[-1][1]
#         path = os.path.join(parent, name)

#         if is_folder:
#             folders.append(path)
#             stack.append((level, path))
#         else:
#             files.append(path)

#     return {
#         "root": root,
#         "folders": folders,
#         "files": files
#     }


import json
import re
import os


# -----------------------------
# Detect tree format
# -----------------------------
def is_tree_format(text):
    return "├──" in text or "└──" in text


# -----------------------------
# Extract JSON from messy text
# -----------------------------
def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return match.group()
    return text


# -----------------------------
# Robust Tree Parser
# -----------------------------
# def parse_tree_structure(text):
#     folders = []
#     files = []

#     lines = [line.rstrip() for line in text.splitlines() if line.strip()]
#     stack = []

#     root = None

#     for line in lines:
#         # Count tree depth based on symbols
#         prefix = re.match(r"^[\s│]*", line).group()
#         level = prefix.count("│") + prefix.count("    ")

#         # Clean tree drawing characters
#         name = re.sub(r"^[\s│]*[├└]──\s*", "", line).strip()

#         # Detect folder
#         is_folder = name.endswith("/") or "." not in name
#         name = name.rstrip("/")

#         if root is None:
#             root = name
#             stack = [(level, name)]
#             continue

#         # Adjust stack based on level
#         while stack and stack[-1][0] >= level:
#             stack.pop()

#         parent = stack[-1][1] if stack else root
#         path = os.path.join(parent, name)

#         if is_folder:
#             folders.append(path)
#             stack.append((level, path))
#         else:
#             files.append(path)

#     return {
#         "root": root,
#         "folders": folders,
#         "files": files
#     }

def parse_tree_structure(text):
    folders = []
    files = []

    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    stack = []

    root = None

    for line in lines:
        # Detect level
        prefix = re.match(r"^[\s│]*", line).group()
        level = prefix.count("│") + prefix.count("    ")

        # Extract name
        name = re.sub(r"^[\s│]*[├└]──\s*", "", line).strip()

        is_folder = name.endswith("/") or "." not in name
        name = name.rstrip("/")

        if root is None:
            root = name
            stack = [(level, "")]  # 🔥 IMPORTANT: empty base
            continue

        while stack and stack[-1][0] >= level:
            stack.pop()

        parent = stack[-1][1] if stack else ""

        path = os.path.join(parent, name) if parent else name

        if is_folder:
            folders.append(path)
            stack.append((level, path))
        else:
            files.append(path)

    return {
        "root": root,
        "folders": folders,
        "files": files
    }


# -----------------------------
# Main Loader
# -----------------------------
def load_input(input_arg):
    """
    Supports:
    - JSON files
    - TXT files
    - raw JSON string
    - messy GPT output
    - tree structures
    """

    # Read input
    if os.path.exists(input_arg):
        with open(input_arg, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = input_arg

    # Clean markdown
    content = content.replace("```json", "").replace("```", "")

    # 🔥 Detect tree structure FIRST
    if is_tree_format(content):
        return parse_tree_structure(content)

    # Otherwise try JSON
    content = extract_json(content)

    try:
        return json.loads(content)
    except Exception as e:
        raise ValueError(f"Invalid JSON or tree format: {e}")