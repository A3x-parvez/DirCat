import os


def create_structure(config, base_path=".", force=False, dry_run=False, verbose=True):
    root = config.get("root", "")

    # Normalize base path
    base_path = os.path.normpath(base_path)

    if root:
        base_path = os.path.normpath(os.path.join(base_path, root))

    actions = []

    # -----------------------------
    # Collect folders
    # -----------------------------
    for folder in config.get("folders", []):
        path = os.path.normpath(os.path.join(base_path, folder))
        actions.append(("dir", path))

    # -----------------------------
    # Collect files
    # -----------------------------
    files = config.get("files", [])

    if isinstance(files, list):
        for file in files:
            path = os.path.normpath(os.path.join(base_path, file))
            actions.append(("file", path, ""))

    elif isinstance(files, dict):
        for file, content in files.items():
            path = os.path.normpath(os.path.join(base_path, file))
            actions.append(("file", path, content or ""))

    # -----------------------------
    # Execute
    # -----------------------------
    dir_count = 0
    file_count = 0
    skipped = 0

    for action in actions:
        if action[0] == "dir":
            path = action[1]

            if verbose:
                print(f"[DIR]  {path}")

            if not dry_run:
                os.makedirs(path, exist_ok=True)

            dir_count += 1

        elif action[0] == "file":
            path, content = action[1], action[2]

            if verbose:
                print(f"[FILE] {path}")

            if not dry_run:
                os.makedirs(os.path.dirname(path), exist_ok=True)

                if os.path.exists(path) and not force:
                    skipped += 1
                    continue

                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

            file_count += 1

    # -----------------------------
    # Summary
    # -----------------------------
    if verbose:
        print("\n📊 Summary:")
        print(f"  📁 Folders: {dir_count}")
        print(f"  📄 Files:   {file_count}")
        if skipped > 0:
            print(f"  ⚠️ Skipped: {skipped} (use --force to overwrite)")
        print("\n✅ Done.\n")