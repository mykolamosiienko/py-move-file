import os


def move_file(command: str) -> None:
    cmd, src, dst = command.split(" ")

    split_path = dst.split("/")
    real_path = "/".join(split_path[:-1])
    real_path_with_file = "/".join(split_path)

    # check if command start with mv
    if cmd.lower() != "mv":
        return

    # rename file
    if "/" not in dst:
        os.rename(src, dst)

    # move file
    elif dst.endswith("/"):
        os.makedirs(real_path, exist_ok=True)
        os.rename(src, real_path + f"/{src}")

    else:
        os.makedirs(real_path, exist_ok=True)
        os.rename(src, real_path_with_file)
