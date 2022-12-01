# License Maker

This project intends to set any code project into an apache licensed project by injecting required headers and adding license file.

It treats files differently according to their extension:

- .sh, .py , .yml, .properties = #
- .java, .scala = /**
- .xml = <--

It checks if a 'LICENSE' file exists and if not, create the one from apache.

It will run through all the files under a directory and if extension matches one of the above, it will add the needed lines.