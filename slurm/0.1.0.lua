help(
[[
This module simply sets the APPTAINER_BIND variable to allows Slurm commands
to be called from within containers.

This module uses the APPTAINER_BIND environmental variable to pass the
necessasry bind mounts. If you are using this variable make sure you append
to avoid overwriting the slurm paths.

The module currently makes sbatch, squeue, and sacct available within the
container. Please contact help@ncsa.illinois.edu if you need additional
commands.
]])

local version = "0.1.0"

whatis("Version: ${version}")

-- find the directory with the slurm.conf file
local slurm_config_dir = "/etc/slurm"
local slurm_config_cache_dir = "/var/spool/slurmd/conf-cache"
if isDir(slurm_config_cache_dir) then
    append_path("APPTAINER_BIND", slurm_config_cache_dir, ",")
else
    append_path("APPTAINER_BIND", slurm_config_dir, ",")
end

-- explicity add each slurm executable
append_path("APPTAINER_BIND", "/usr/bin/sbatch,/usr/bin/squeue,/usr/bin/sacct", ",")

-- add necessary support files
append_path("APPTAINER_BIND", "/usr/lib64/slurm,/etc/passwd,/etc/group", ",")

-- add necessary munge files
append_path("APPTAINER_BIND", "/lib64/libmunge.so.2,/run/munge", ",")
