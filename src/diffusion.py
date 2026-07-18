"""
diffusion.py
---------------------------------
Sulfide diffusion through bentonite
"""


def effective_sulfide(
    sulfide,
    diffusion_factor
):
    """
    Calculates sulfide reaching the copper surface.
    """

    return sulfide * diffusion_factor