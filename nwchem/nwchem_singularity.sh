{% extends "bases/shell-script-base.sh" %}

# Wrapper that enters the container via the SHPC exec script and launches MPI inside

{% block content %}
# Set NUM_PROCS if not already defined
if [ -z "$NUM_PROCS" ]; then
  if [ -n "$SLURM_NTASKS" ]; then
    NUM_PROCS=$SLURM_NTASKS
  else
    NUM_PROCS=$(nproc)
  fi
fi

LAUNCHER="mpiexec -n ${NUM_PROCS}"

# Locate the SHPC-generated Singularity exec wrapper
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTAINER_EXEC=$(ls "${SCRIPT_DIR}"/nwchem-*-exec 2>/dev/null | head -n 1)

if [ -z "$CONTAINER_EXEC" ]; then
  echo "Error: Could not find nwchem-*-exec in ${SCRIPT_DIR}" >&2
  exit 1
fi

# Run the launcher *inside* the container using the wrapper
"$CONTAINER_EXEC" ${LAUNCHER} nwchem \
{% if '/sh' in settings.wrapper_shell or '/bash' in settings.wrapper_shell %}"$@"\
{% elif '/csh' in settings.wrapper_shell %}$argv:q\
{% endif %}

{% endblock %}

