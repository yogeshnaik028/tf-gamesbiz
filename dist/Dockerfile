# ------------------------------------------------------------------------------
# Main
# =======
# Can be used as base image for regular training job executions
# ------------------------------------------------------------------------------

FROM python:3.6-slim

# Add standard build tools and libraries
RUN apt-get -y update && apt-get install -y --no-install-recommends \
    build-essential \
    unixodbc-dev \
    libboost-python-dev \
    ca-certificates

# Install any package-specific python requirements
RUN pip install numpy scipy pandas scikit-learn tensorflow

# Copy over entrypoint script and define image entry
COPY run.py /opt/run.py
ENTRYPOINT ["python", "/opt/run.py"]

# Copy and install training code
COPY gamesbiz-0.0.1rc0.tar.gz /opt/gamesbiz-0.0.1rc0.tar.gz
RUN pip install /opt/gamesbiz-0.0.1rc0.tar.gz