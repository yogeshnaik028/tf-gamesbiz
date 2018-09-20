#!/usr/bin/env bash
export entry_point=$(ps -ef | awk '/entry_point={/{flag=1;next}/}/{flag=0}flag { print $1 }' setup.py )
export module_name=$(sed -e 's/^"//' -e 's/"$//' <<< "$( cut -d':' -f1 <<<"$entry_point")")
export function_name=$(sed -e 's/^"//' -e 's/"$//' <<< "$( cut -d':' -f2 <<<"$entry_point")")
python3 setup.py egg_info
export pkg_name=$(ps -ef | awk '{ if ($1 ~ /Name:/) print $2}' *.egg-info/PKG-INFO)
export pkg_version=$(ps -ef | awk '{ if ($1 ~ /^Version:/) print $2}' *.egg-info/PKG-INFO)
if [ -f "$pkg_name.egg-info/requires.txt" ]; then
   echo "requires.txt file exists."
else
   echo "requires.txt file exists."
fi
export dependencies=""
while read -r line
do
     dependencies="$dependencies""$line "
done < "$pkg_name.egg-info/requires.txt"
python3 setup.py sdist
cd dist
echo "# ------------------------------------------------------------------------------" >> Dockerfile
echo "# Main" >> Dockerfile
echo "# =======" >> Dockerfile
echo "# Can be used as base image for regular training job executions" >> Dockerfile
echo "# ------------------------------------------------------------------------------" >> Dockerfile
echo "" >> Dockerfile
echo "FROM python:3.6-slim" >> Dockerfile
echo "" >> Dockerfile
echo "# Add standard build tools and libraries" >> Dockerfile
echo "RUN apt-get -y update && apt-get install -y --no-install-recommends \ " >> Dockerfile
echo "    build-essential \ " >> Dockerfile
echo "    unixodbc-dev \ " >> Dockerfile
echo "    libboost-python-dev \ " >> Dockerfile
echo "    ca-certificates \ " >> Dockerfile
echo "" >> Dockerfile
echo "# Install any package-specific python requirements" >> Dockerfile
echo "RUN pip install $dependencies" >> Dockerfile
echo "" >> Dockerfile
echo "COPY run.py /opt/run.py" >> Dockerfile
echo "ENTRYPOINT ['"'python'"', '"'/opt/run.py'"']" >> Dockerfile
echo "" >> Dockerfile
echo "# Copy and install training code" >> Dockerfile
echo "COPY $pkg_name-$pkg_version.tar.gz /opt/$pkg_name-$pkg_version.tar.gz" >> Dockerfile
echo "from $module_name import $function_name" >> run.py
echo "$function_name()" >> run.py
