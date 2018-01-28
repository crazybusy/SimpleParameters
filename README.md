Simple parsing of parameters supplied on the command line

Allows to create json file with details of the parameters available on the command line for any application. It then handles the user parsing of these parameters by setting the required flags which you can directly consume in your application

Get started by creating an object of SimpleParameters by creating its object

params = SimpleParameters('path to configuration files')

options, args = params.resolve_parameters(sys.argv)

Now the command line swtiches specifed in the json file are available in the options list and the positional parameters are available as args. It generates the help files etc. Try using -h option

Refer the SimpleParameters.txt for an example of the json parameters template
