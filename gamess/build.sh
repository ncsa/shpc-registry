#!/bin/sh
#SBATCH --cpus-per-task=4 --mem 16GB -t 240

apptainer build ~/scratch-global/gamess.00.sif gamess.def
