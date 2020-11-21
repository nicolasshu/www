---
layout: article
title: "Slurm Commands"
tags:
  - Instructions
  - Server
permalink: /slurm_commands.html
mathjax: false
---

Here is a quick reminders on [Slurm](https://slurm.schedmd.com/) and how to use it

## One Line Commands

### View the Running Jobs
```
$ squeue
   JOBID  PARTITION             NAME     USER   ST       TIME     NODES    NODELIST(REASON)
   26529      batch       train_BERT      joe    R    1:24:52         1              cnode1
   26530      batch     train_ResNet    maria    R    2:12:56         1              cnode2
   26531      batch      update_plex    maria    R    2:14:20         1              cnode3
   26532      batch    download_data    janet    R    2:16:17         1              cnode7
```

### View Nodes and Partitions

```
$ sinfo
PARTITION    AVAIL  TIMELIMIT  NODES  STATE NODELIST
batch*          up 8-00:00:00      9    mix cnode[1-9]
batch*          up 8-00:00:00      3   idle cnode[10-12]
gpu             up 8-00:00:00      9    mix cnode[1-9]
gpu             up 8-00:00:00      3   idle cnode[10-12]
rtx             up 8-00:00:00      4   idle rnode[1-4]
reservations    up   infinite      1  down* nvidia-dgx1
reservations    up   infinite     10    mix beauty,cnode[1-9]
reservations    up   infinite      7   idle cnode[10-12],rnode[1-4]
overflow        up   infinite      1  down* nvidia-dgx1
overflow        up   infinite     10    mix beauty,cnode[1-9]
overflow        up   infinite      7   idle cnode[10-12],rnode[1-4]
```

## Submitting a Job

You can submit either a job or open an interactive bash, and then run your job through there

### Running a Job with sbatch

First create a shell script that will be used

```shell
# run.sh

#!/bin/bash
#SBATCH --job-name  {job_name}         # E.g. train_model
#SBATCH --nodelist  {node_name}        # E.g. cnode1
#SBATCH --partition {partition_name}   # E.g. gpu
#SBATCH --gpus      {number_of_gpus}   # E.g. 1
#SBATCH --time      {max_time}         # E.g. 08-00
#SBATCH --ntasks    {number_of_cpus}   # E.g. 16
#SBATCH --mem       {ram_memory}       # E.g. 32G

# Enable using a python 
scl enable rh-python36 bash
source /home/user/envs/myenv/bin/activate

# Copy data into your /tmp folder (Read below)
cp /home/user/data/my_dataset /tmp/user/my_dataset

# Copy your script
cp my_experiment.py /tmp/user

# Change into that directory
cd /tmp/user

# Run your script
python my_experiment.py
```

Sometimes, job is deployed at a different node than that of where you originally are. For example, if you are on `cnode0`, sometimes the job gets deployed at another node (e.g. `cnode1`). This can be seen in your terminal, which should say `user@cnode0`. With that, the `/tmp` directory in different nodes are not the same. In other words, `cnode0`'s `/tmp` directory is not the same as `cnode1`'s `/tmp`. Therefore, if you are dealing with a dataset, it is not wise to have the server to get data from another computer every time. So, it's helpful to copy that dataset into the `/tmp` directory

Finally, you can run the job with 

```bash
sbatch run.sh
```

Below is the same script as the one above, but using the shortened flags 

```shell
# run.sh

#!/bin/bash
#SBATCH -J       {job_name}         # E.g. train_model
#SBATCH -w       {node_name}        # E.g. cnode1
#SBATCH -p       {partition_name}   # E.g. gpu
#SBATCH -G       {number_of_gpus}   # E.g. 1
#SBATCH -t       {max_time}         # E.g. 08-00
#SBATCH -n       {number_of_cpus}   # E.g. 16
#SBATCH --mem    {ram_memory}       # E.g. 32G

# Enable using a python 
scl enable rh-python36 bash
source /home/user/envs/myenv/bin/activate

# Copy data into your /tmp folder (Read below)
cp /home/user/data/my_dataset /tmp/user/my_dataset

# Copy your script
cp my_experiment.py /tmp/user

# Change into that directory
cd /tmp/user

# Run your script
python my_experiment.py
```


### Run a Job with srun

This is the way you can run a job interactively. Basically, a lot of the above is done again, but just interactively.

First you need to get into the interactive bash. The `--pty` flag in `srun` allows you to execute a task in a pseudo terminal mode

```bash
user@cnode0:~$ srun -J jobname -p gpu -G 1 -w cnode7 -n 10 --mem 16G --pty bash
# or srun -J jobname -p batch -G 1 -w cnode7 -n 10 --mem 16G --pty bash
user@cnode7:~$
```

Then you can run your jobs as you normally would. E.g. 


```bash
user@cnode7:~$ cp /home/user/data/my_dataset /tmp/user
user@cnode7:~$ source /home/user/envs/myenv/bin/activate
user@cnode7:~$ cp my_experiment.py /tmp/user
user@cnode7:~$ cd /tmp/user
user@cnode7:~$ python my_experiment.py
```


## Additional Resources

- [Slurm's Quick Start User Guide](https://slurm.schedmd.com/quickstart.html)

An example written by Jim Kinney and Robert Tweedy is 


```shell
#!/bin/bash

# This is an example SBATCH script "slurm_example_script.sh"
# For all available options, see the 'sbatch' manpage.
#
# Note that all SBATCH commands must start with a #SBATCH directive;
# to comment out one of these you must add another # at the beginning of the line.
# All #SBATCH directives must be declared before any other commands appear in the script.
#
# Once you understand how to use this file, you can remove these comments to make it
# easier to read/edit/work with/etc. :-)

### (Recommended)
### Name the project in the batch job queue
#SBATCH -J ExampleName

### (Optional)
### If you'd like to give a bit more information about your job, you can
### use the command below.
#SBATCH --comment='A comment/brief descriptive name of your job goes here.'

### (REQUIRED)
### Select the queue (also called "partition") to use. The available partitions for your
### use are visible using the 'sinfo' command.
### You must specify 'gpu' or another partition to have access to the system GPUs.
#SBATCH -p batch

### (REQUIRED for GPU, otherwise do not specify)
### If you select a GPU queue, you must also use the command below to select the number of GPUs
### to use. Note that you're limited to 1 GPU per job as a maximum on the basic GPU queue.
### If you need to use more than 1, contact bmi-it@emory.edu to schedule a multi-gpu test for
### access to the multi-gpu queue.
###
### If you need a specific type of GPU, you can prefix the number with the GPU's type like
### so: "SBATCH -G turing:1". The available types of GPUs as of 04/16/2020 are:
### turing (12 total)
### titan (only 1; requesting this GPU may result in a delay in your job starting)
### pascal (4 total; using this GPU requires that your code handle being pre-empted/stopped at any
###        time, as there are certain users with priority access to these GPUs).
### volta (8 total) - You must use the 'dgx-only' partition to select these GPUs.
### rtx (4 total) - NVidia Quadro RTX 6000. You must use the 'rtx' or 'overflow' partitions to select these GPUs.
##SBATCH -G 1

### (REQUIRED) if you don't want your job to end after 8 hours!
### If you know your job needs to run for a long time or will finish up relatively
### quickly then set the command below to specify how long your job should take to run.
### This may allow it to start running sooner if the cluster is under heavy load.
### Your job will be held to the value you specify, which means that it will be ended
### if it should go over the limit. If you're unsure of how long your job will take to run, it's
### better to err on the longer side as jobs can always finish earlier, but they can't extend their
### requested time limit to run longer.
###
### The format can be "minutes", "hours:minutes:seconds", "days-hours", or "days-hours:minutes:seconds".
### By default, jobs will run for 8 hours if this isn't specified.
#SBATCH -t 8:0:0


### (optional) Output and error file definitions. To have all output in a file named
### "slurm-<jobID>.out" just remove the two SBATCH commands below. Specifying the -e parameter
### will split the stdout and stderr output into different files.
### The %A is replaced with the job's ID.
#SBATCH -o file-%A.out
#SBATCH -e file-%A.err

### You can specify the number of nodes, number of cpus/threads, and amount of memory per node
### you need for your job. We recommend specifying only memory unless you know you need a
### specific number of nodes/threads, as you will be automatically allocated a reasonable
### amount of threads based on the memory amount requested.

### (REQUIRED)
### Request 4 GB of RAM - You should always specify some value for this option, otherwise
###                       your job's available memory will be limited to a default value
###                       which may not be high enough for your code to run successfully.
###                       This value is for the amount of RAM per computational node.
#SBATCH --mem 4G

### (optional)
### Request 4 cpus/threads - Specify a value for this function if you know your code uses
###                          multiple CPU threads when running and need to override the
###                          automatic allocation of threads based on your memory request
###                          above. Note that this value is for the TOTAL number of threads
###                          available to the job, NOT threads per computational node! Also note
###                          that Matlab is limited to using up to 15 threads per node due to
###                          licensing restrictions imposed by the Matlab software.
##SBATCH -n 4

### (optional)
### Request 2 cpus/threads per task - This differs from the "-n" parameter above in that it
###                                   specifies how many threads should be allocated per job
###                                   task. By default, this is 1 thread per task. Set this
###                                   parameter if you need to dedicate multiple threads to a
###                                   single program/application rather than running multiple
###                                   separate applications which require a single thread each.
##SBATCH -c 2

### (very optional; leave as '1' unless you know what you're doing)
### Request 1 node - Only specify a value other than 1 for this option when you know that
###                  your code will run across multiple systems concurrently. Otherwise
###                  you're just wasting resources that could be used by others.
#SBATCH -N 1

### (optional)
### This is to send you emails of job status
### See the manpage for sbatch for all the available options.
#SBATCH --mail-user=nicolas.s.shu@gmail.com
#SBATCH --mail-type=ALL

### Your actual commands to start your code go below this area. If you need to run anything in
### the SCL python environments that's more complex than a simple Python script (as in, if you
### have to do some other setup in the shell environment first for your code), then you should
### write a wrapper script that does all the necessary steps and then run it like in the below
### example:
###
### scl enable rh-python36 '/home/mynetid/my_wrapper_script.sh'
###
### Otherwise, you're probably not running everything you think you are in the SCL environment.
hostname
echo 'Hello world!' > test.txt
scl enable rh-python36 'python shit.py' > shit.txt
```