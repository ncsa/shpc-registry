# Use Ubuntu Jammy as the base image
FROM ubuntu:jammy

# Define the ARG for the download URL
ARG MMSEQS_URL=https://dev.mmseqs.com/latest/mmseqs-linux-gpu.tar.gz

# Install necessary packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    wget \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Download and extract the mmseqs-linux-avx2.tar.gz file
RUN wget ${MMSEQS_URL} -O /tmp/mmseqs.tar.gz \
    && tar -xzf /tmp/mmseqs.tar.gz -C /opt \
    && rm /tmp/mmseqs.tar.gz

# Add the mmseqs binary to the PATH
ENV PATH="/opt/mmseqs/bin:${PATH}"

# Default command
CMD ["mmseqs"]
