import torch.nn.functional as F

from ..registry import LOSSES
from .base import BaseWeightedLoss


@LOSSES.register_module
class NLLLoss(BaseWeightedLoss):
    """NLL Loss.

    It will calculate NLL loss given cls_score and label.
    """

    def _forward(self, cls_score, label, **kwargs):
        loss_cls = F.nll_loss(cls_score, label, **kwargs)
        return loss_cls
