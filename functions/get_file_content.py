import os


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir
    if file_path:
        target_file = os.path.abspath(
            os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" is not a file'
    try:
        MAX_CHARS = 10000

        with open(target_file, "r") as f:
            file_contents = f.read(MAX_CHARS)
            return file_contents
    except Exception as e:
        return f"Error: {e}"
