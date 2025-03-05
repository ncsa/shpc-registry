Original images based on https://github.com/cp2k/cp2k-containers.

OpenMPI is built inside the container and should not require an external mpi library. The 'munge' variant include 
the munge library but /etc/munge/munge.key may need to be bind mounted when the running the container to avoid
warning messages.

WARNING: this may not work on a multinode mpi run
