---
layout: page
title: "Using a Cluster"
categories:
  - Instructions
---

# How to Submit Jobs a the Cluster

This is completely with the help of Alvince Pongos, aka Master of Clusters.  

## Login to a Node via SSH
First you need to be in one of the nodes in order to work remotely. In this case you can use your username  

```
$ ssh username@stuff.stuff.stuff.stuff
```

## MATLAB
### Compile an Executable 
To run MATLAB scripts, you will often have to compile your .m scripts into an executable. For UNIX systems, you will likely use a .sh file, where as in Windows machines, you'll likely use a .exe file.   

When in your working directory, to compile your `filename.m` script, run the following line:  
```
$ mcc -mv filename.m -R nodisplay
```

In case you have any `addpath()` function in your script, it's advisable to put the flag `-a` in order to add specific files, or to add any folder and its subfolders to path. E.g. 
```
$ mcc -mv filename.m -R nodisplay -a ./MyToolbox_of_Tools
```

The `mcc` function is a MATLAB compiler (see the [documentation](https://www.mathworks.com/help/compiler/mcc.html)). Its syntax follows `mcc options mfilename1 mfilename2...mfilenameN`  

The `-m` flag compiles the function into a standalone application.   
The `-v` flag displays the compilation steps (e.g. MATLAB compiler version number, the source file names as they ar processed, the invocation of `mbuild`, the names of the generated output files as they are created).  
The `filename.m` is the desired file for which you wish to setup an executable.
The `-R` flag provides MATLAB runtime options  

| Option | Description | Target  |
| :----: |:-----------:| :------:|
| -logfile,filename	| Specify a log file name.                                    | MATLAB Compiler |
| -nodisplay            | Suppress the MATLAB nodisplay run-time warning.             | MATLAB Compiler |
| -nojvm                | Do not use the Java Virtual Machine (JVM).                  | MATLAB Compiler |
| -startmsg             | Customizable user message displayed at initialization time. | MATLAB Compiler Standalone Applications |
| -completemsg	        | Customizable user message displayed when initialization is complete. | MATLAB Compiler Standalone Applications |

There are more options, but you can see them in [MATLAB's Documentations](https://www.mathworks.com/help/compiler/mcc.html#butdlms-1)  

After this point you are likely to have a `run_filename.sh` file (if running on a UNIX machine).   

### Make Executable Wrappers

At this point, you are to create one or two different executables such that they can submit the job to the cluster. If using two scripts, their functions are as follows:  

1. **Master Script** - The first script submits the jobs that are on the second script as `qsub` jobs  
1. **Chain Script** - The second script has chain jobs such that would in turn run the executables created previously  

#### MasterScript.sh
```
#!/bin/bash
echo "Message to yourself. Hello!"
qsub -N "Title_For_Cluster" working/directory/of/chain/script/ChainScript.sh
```

#### ChainScript.sh
```
#!/bin/bash
#PBS -q batch
#PBS -d /working/directory/where/compiled/script/is/located/
#PBS -o outputFolder
#PBS -e errorFolder
#PBS -l nodes=1:ppn=4:pascal,walltime=168:00:00

workDir="/working/directory/where/compiled/script/is/located/"
"$workDir"run_filename.sh /opt/matlab/MCR/2017b/
```

In the example above, the **MasterScript.sh** sends a `qsub` job that will be named 'Title_For_Cluster'. The job that is being sent is the **ChainScript.sh**.  

The **ChainScript.sh** is the one that runs your executable compiled script. Remember how we compiled a script that is called `run_filename.sh`? That will now be run. However, with MATLAB, you need to specify the location of `matlab*`. In this case, it is at `/opt/matlab/MCR/2017b/`

The `#PBS` is not hashtag phosphate buffered saline. We're done with that. It stands for *Portable Batch System*(PBS)  

The `-q` flag defines the destination of the job. It may be `batch` or `gpu`.  
The `-o` flag defines the path to be used for the standard output stream of the batch job.  
The `-e` flag defines the path to be used for the standard error stream of the batch job.  
The `-d` flag defines the path of the working directory.  
The `-l` flag defines the resources that are required by the job. It establishes a limit to the amount of resources that it can be consumed. In case this is not set, then the PBS scheduler uses the default values set by the system administrator.  

In this case, it is `nodes=1:ppn=4:pascal,walltime=168:00:00`
* `nodes` is the number of nodes that will be used;
* `ppn` is the number of processors per node that will be used;
* `walltime` is the maximum amount of time for which the job can run;
* (Special:: `pascal` is the keyword that sends it to Beauty).


### Ready? Set? Go!

Are you ready? Now just run the **MainScript.sh** with `bash`!
```
$ bash MainScript.sh
```

While waiting, you can check to see the status of your job by going to your Terminal and running
```
$ qstat

Job ID                    Name              User            Time Use S Queue
------------------------- ----------------  --------------- -------- - -----
19285.node0.cluster.crap  Title_For_Cluster username        22:00:56 R batch          
19339.node1.mustard.crap  CrappyJob         MrCrap          23:07:16 R batch          
19347.node2.plumber.crap  OhShit            MrFool          15:45:46 C batch          
19379.node6.buster.crap   PleaseWork        MsUnhappy       07:55:29 R batch  
```

In this example, since you are called `username`, that is the first job in the cluster. Its job ID is 19285. It has been running for 22:00:56, and its status (S) is `R` for running

`MrFool`'s job however has already been completed since the status is `C` for complete
`MsUnhappy` in the other hand... is unhappy... That's sad. 

If you then go to the folder `outputFolder/`, you may later find a file called `Title_For_Cluster.e19285`, which will show the errors for your job. If you instead see `Title_For_Cluster.o19285`, it will show the outputs for your job. 

Now, it's time to debug!

### Additional Resources

Here are a few additional resources
* [Running a Job on HPC using PBS](https://hpcc.usc.edu/support/documentation/running-a-job-on-the-hpcc-cluster-using-pbs/)
* [Albert Kim's Tutorial](https://albertsk.files.wordpress.com/2011/12/pbs.pdf)

