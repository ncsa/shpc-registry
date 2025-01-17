# Use rocker/verse as the base image
FROM rocker/verse:latest

# Set environment variables for non-interactive installations
ENV DEBIAN_FRONTEND=noninteractive

# Install build tools and dependencies
RUN apt-get update && apt-get install -y \
    curl \
    bzip2 \
    autoconf \
    automake \
    make \
    gcc \
    perl \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libssl-dev \
    libncurses5-dev \
    libdeflate-dev \
    libfontconfig1-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libcurl4-openssl-dev \
    libfreetype6-dev \
    libpng-dev \
    libtiff5-dev \
    libjpeg-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Download, build, and install samtools
WORKDIR /usr/local/src
RUN curl -LO https://github.com/samtools/samtools/releases/download/1.21/samtools-1.21.tar.bz2 \
    && tar -xjf samtools-1.21.tar.bz2 \
    && cd samtools-1.21 \
    && ./configure \
    && make \
    && make install \
    && cd .. && rm -rf samtools-1.21 samtools-1.21.tar.bz2

# Install R packages
RUN R -e "install.packages(c('devtools', 'remotes', 'BiocManager', 'R.utils'))" \
    && R -e "BiocManager::install(c('Rsamtools', 'Rbowtie2'))" \
    && R -e "remotes::install_github(c('ropensci/bold', 'ropensci/taxize'))"

RUN R -e "BiocManager::install('MetaScope')" 



# Set working directory
WORKDIR /home

# Default command
CMD ["/bin/bash"]
