import torch
import torch.nn as nn
import torch.nn.init as init




def reset_model_weights(model):
    """
    Reinitialize all layers in a PyTorch model with random weights 
    and ensure requires_grad is True for all parameters.
    
    Args:
        model (nn.Module): The PyTorch model to reset.
    """
    def init_weights(layer):
        """Reset weights of a given layer to random initialization."""
        if hasattr(layer, 'reset_parameters'):
            layer.reset_parameters()  # Default PyTorch reset
        elif isinstance(layer, nn.Linear):
            init.xavier_uniform_(layer.weight)
            if layer.bias is not None:
                init.zeros_(layer.bias)
        elif isinstance(layer, nn.Conv2d):
            init.kaiming_normal_(layer.weight, mode='fan_out', nonlinearity='relu')
            if layer.bias is not None:
                init.zeros_(layer.bias)
    
    # Apply the weight reset function to all layers
    model.apply(init_weights)
    
    # Ensure requires_grad is True for all parameters
    for param in model.parameters():
        param.requires_grad = True

    print("Model weights reinitialized and requires_grad set to True!")


