import torch
from torch.utils.data import DataLoader
from pathlib import Path


class Trainer:

    def __init__(
        self,
        model,
        dataset,
        lr=5e-5,
        batch_size=4,
        device=None
    ):

        self.device = device or (
            "cuda" if torch.cuda.is_available()
            else "cpu"
        )

        self.model = model.to(
            self.device
        )


        self.loader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=True
        )


        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=lr
        )


    def train(
        self,
        epochs=1
    ):

        self.model.train()


        for epoch in range(epochs):

            total_loss = 0


            for batch in self.loader:

                input_ids = batch[
                    "input_ids"
                ].to(self.device)


                labels = batch[
                    "labels"
                ].to(self.device)


                outputs = self.model(
                    input_ids,
                    labels=labels
                )


                loss = outputs.loss


                self.optimizer.zero_grad()

                loss.backward()

                self.optimizer.step()


                total_loss += loss.item()


            avg_loss = (
                total_loss /
                len(self.loader)
            )


            print(
                f"Epoch {epoch+1} Loss: {avg_loss}"
            )


    def save(
        self,
        path="checkpoints/genesisllm.pt"
    ):

        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )


        torch.save(
            self.model.state_dict(),
            path
        )


        print(
            f"Model saved: {path}"
        )