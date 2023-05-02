# Load the 'utils' package
library(utils)

# Get the list of installed packages
installed_packages <- installed.packages()

# Extract package names from the list
package_names <- installed_packages[, "Package"]

# Print the package names to stdout
cat(package_names, sep = "\n")
