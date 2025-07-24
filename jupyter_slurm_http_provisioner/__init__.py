"""
jupyter_slurm_provisioner

This package registers slurm_http_provisioner endpoint.

    pip install jupyter-slurm-http-provisioner
    # check endpoints
    jupyter kernelspec provisioners
"""
from .http_provisioner import SlurmHTTPProvisioner

VERSION = "0.4.0"
