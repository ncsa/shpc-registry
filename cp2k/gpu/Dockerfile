FROM jterstriep/cp2k:2025.1_openmpi_generic_cuda_A100_psmp

RUN apt-get update && apt-get install -y \
    libmunge-dev \
    libmunge2 \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV OMPI_MCA_plm=isolated
#ENV OMPI_MCA_orte_launch_agent="singularity exec /path/to/container.sif orted"
