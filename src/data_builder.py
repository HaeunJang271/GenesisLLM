import json
from pathlib import Path


class DataBuilder:

    def __init__(self):

        self.output = Path("../data/processed/train.jsonl")

    def build_from_text(self, text):

        self.output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.output,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "text": text
                },
                f,
                ensure_ascii=False
            )

            f.write("\n")


if __name__ == "__main__":

    builder = DataBuilder()

    builder.build_from_text(

        """
대한민국의 수도는 서울이다.

Qwen은 공개 언어 모델이다.

Transformer는 Self Attention을 사용한다.
        """

    )

    print("완료")