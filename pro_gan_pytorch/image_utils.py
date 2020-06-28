from typing import Optional, Tuple

import numpy as np

import torch
from torch import Tensor


def adjust_dynamic_range(
    data: Tensor,
    drange_in: Optional[Tuple[int, int]] = (-1, 1),
    drange_out: Optional[Tuple[int, int]] = (0, 1),
):
    if drange_in != drange_out:
        scale = (np.float32(drange_out[1]) - np.float32(drange_out[0])) / (
            np.float32(drange_in[1]) - np.float32(drange_in[0])
        )
        bias = np.float32(drange_out[0]) - np.float32(drange_in[0]) * scale
        data = data * scale + bias

    return torch.clamp(data, min=drange_out[0], max=drange_out[1])
