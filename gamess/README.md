
## Building and Installing the Latest GAMESS Release with SLURM

To obtain, build, and install the most recent release of GAMESS using SLURM, follow the steps below:

1. **Download GAMESS**: Follow the directions on this 
[download link](https://www.msg.chem.iastate.edu/GAMESS/download/dist.source.shtml). You'll have to register and recieve an email with the password.

2. **Create a custom rungms**: The rungms command provided attempts determine
which environment it's running and "do the right thing". Unfortuantely,
this doesn't necessarily match our environment. 

There are two special considerations, the setting of SCR and USERSCR
environmental variables and the use of SLURM commands within the script.

**SCR** specifies the scratch directory  where temporary files will be
written. **USERSCR** specifies where restart files will be written. The
inspections of the environment code was replaced with a simple check
to see if variables was defined, providing a reasonable default if not.
The script also checks if the given directory exists and creates it if
necessary.

Rungms uses **srun** and **scontrol** during its execution. Because it
is running inside a container it fails to find the host SLURM commands. The 
**scontrol** command is used to list the nodes assigned to the job and
can safely be replaced with an 'echo $SLURM_JOB_NODELIST'. The **srun** is
used to run some setup and teardown commands as seperate steps. The **srun**
can safely be removed.

*A custom rungms is provided will replace the rungms distributed with
GAMESS. Rungms is will like change with each GAMESS release so you may
want to manually compare with original rungms (stored as rungms.orig) 
and adjust as necessary.*

2. **Build container with build.sh**: This script will build a container
in your scratch space. 

    ```bash
    sbatch build.sh
    ```

This script asks for 4 cores which speeds up the build process.

3. **Test container with test.sh**: 
    ''

3. **Copy the GAMESS container**: Once the build completes, check for errors
in the job output. If everything looks good copy the container to somewhere
world readable such as /tmp.


    ```bash
    cp -r ~/scratch-global/gamess.00.sif /tmp
    chmod a+r /tmp/gamess.00.sif
    ```

The build process seems very sensetive to compiler versions, etc. The def
file will help but will likely break for future versions.

4. **Install with shpc**: install

    ```bash
    conda activate shpc
    shpc install gamess:*version* /tmp/gamess.00.sif
    publish_containers
    ```

5. **Clean-up**: Remove the container from /tmp and save the GAMESS tar file
*somewhere*. We don't have a good place for this as of right now. It's
probably ok in ~/svcmgswmgt/shpc-registry/gamess for now but we don't want
to commit it to the repository. 

