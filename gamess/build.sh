#!/bin/sh
#SBATCH --cpus-per-task=4 --mem 16GB -t 240

if [ -z "$CONTAINER" ]; then
    CONTAINER="$HOME/scratch-global/gamess.00.sif"
fi

if [ -f $CONTAINER ]; then
    rm $CONTAINER
fi

apptainer build $CONTAINER gamess.def

echo "======== comparing rungms =========="
apptainer exec $CONTAINER diff /opt/gamess/rungms.orig /opt/gamess/rungms
