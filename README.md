# Slurm HTTP Provisioner

## What is this package

This package is a Jupyter Kernel Provisioner.

It uses an http(s) api to launch a remote kernel in a slurm job and ssh tunnels to connect to it.

Once configured, on the Jupyter Notebook / Lab interface, you can just select a kernel using this provisioner and it will set up everything accordingly.

## Setup

`pip install jupyter-slurm-http-provider`

### 1 - Build an api

5 endpoints are mandatory :

- GET - /pub_key -> returns the public ssh key of the compute node that runs the kernel
- POST - /launch_kernel -> launches a kernel in a slurm job
- GET - /ready -> returns the state of the slurm job, and if started, returns the kernel's connection file
- POST - /start_tunnels -> should establish ssh tunnels between the compute node and the notebook, optionally mount folders
- DELETE - /tunnels -> called during cleanup, after the tunnels are closed. It could start a garbage collector

### 2 - Set up a kernel

This is the kernel that will use the slurm-http-provisioner. Its name will be displayed in the Notebook / Lab interface.

```
#~/.local/share/jupyter/kernels/slurm-http/kernel.json
{
  "display_name": "Python 3 (Slurm HTTP)",
  "language": "python",
  "metadata": {
    "kernel_provisioner": {
      "provisioner_name": "slurm-http-provisioner",
      "config": {
        "url": "http://example.com",
        "api_key": "1234",
        "username": "xxxx",
        "hostname": "xxx.xxx.xxx.xxx"
      }
    }
  }
}

```

See the example file

### 3 - Voilà

You should now be able to use this new kernel.

Use `jupyter kernelspec list` to check your kernel is detected.
Use `jupyter kernelspec provisioners` to check that slurm-http-provisioner is installed.
