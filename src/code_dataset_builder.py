
from pathlib import Path


def build_code_dataset(
    input_file="data/raw/python_expanded.txt",
    output_file="data/code_train.txt"
):

    text = Path(input_file).read_text(
        encoding="utf-8"
    )


    Path(output_file).write_text(
        text,
        encoding="utf-8"
    )


    print(
        "Created:",
        output_file
    )

    print(
        "Characters:",
        len(text)
    )


if __name__ == "__main__":

    build_code_dataset()
