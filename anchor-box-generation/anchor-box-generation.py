import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    
    stride = image_size / feature_size
    ws, hs = list(), list()
    for s in scales:
        for r in aspect_ratios:
            ws.append(s * r ** 0.5)
            hs.append(s / r ** 0.5)
            
    result = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride

            for w, h in zip(ws, hs):
                anchor = [[cx - w/2, cy - h/2, cx + w/2, cy + h/2]]
                result += anchor

    return result