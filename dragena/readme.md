The dragena tar file must be specified using the environmental variable DRAGENA_TAR 
during the singularity build command. 

```bash
export DRAGENA_TAR=/usr/apps/install_files/dragena-linux-x64-DAv1.1.0-rc3.tar.gz 
singularity build dragena.sif dragena.def
```

- The def file untars the files into /opt/dragena 
- /opt/dragena is added to the PATH.
- The executable is located at /opt/dragena/dragena.
- The top level directory from the tar file is stripped.
