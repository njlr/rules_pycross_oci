import torch

print(f"Torch Version: {torch.__version__}")

hello_tensor = torch.tensor([[1, 2], [3, 4]])
print(hello_tensor)

if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

print(f"\nUsing device: {device.upper()}")

hello_tensor = hello_tensor.to(device)
