import difflib


def generate_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.readlines()
        content2 = f2.readlines()
        differ = difflib.unified_diff(content1, content2, fromfile=file1, tofile=file2)
        diff_content = '\n'.join(differ)
        with open("diff_file.diff", 'w') as diff_file:
            diff_file.write(diff_content)
        print("Diff file 'diff_file.diff' created successfully.")


# ************ Files Difference ************
file1 = "file1.txt"
file2 = "file2.txt"
generate_diff(file1, file2)
