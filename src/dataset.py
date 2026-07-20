from pathlib import Path
from torch.utils.data import Dataset
import torch


class TextDataset(Dataset):
    """
    GPT/Qwen Continued Pretraining용 TXT 데이터셋
    """

    def __init__(self, tokenizer, file_path, block_size=256):

        self.examples = []

        file_path = Path(file_path)

        text = file_path.read_text(
            encoding="utf-8"
        )

        tokens = tokenizer.encode(text)

        for i in range(
            0,
            len(tokens) - block_size,
            block_size
        ):

            self.examples.append(
                tokens[i:i + block_size]
            )

    def __len__(self):

        return len(self.examples)

    def __getitem__(self, idx):

        x = torch.tensor(
            self.examples[idx],
            dtype=torch.long
        )

        return {
            "input_ids": x,
            "labels": x.clone()
        }