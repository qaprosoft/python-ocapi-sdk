"""

This module will do the following:

    - Depend on the sfcc-ci-linux module: https://github.com/SalesforceCommerceCloud/sfcc-ci#linux
    - Will install sfcc module via download to the docker container: https://source.digital.accenture.com/projects/PAN/repos/pandora-automation/browse
    - Will also install via NPM
    - We will authorize using credentials provided

        *sfcc-ci-linux client:auth

    - We will parse the stdout of the below to grab the job status

        *sfcc-ci-linux instance:export -i <instance_uri> -d '{"global_data":{"meta_data":true}}' -f site_meta

        (STDOUT): sfcc-ci-linux job:status "sfcc-site-archive-export" "<job-id>" -i <instance.uri>

    - We will then call the above and wait for "finsihed (OK)" in the return data*

    - We will auth into the export endpoint:

        *https://<instance-domain>.demandware.net/on/demandware.servlet/webdav/Sites/Impex/src/instance

    - Download the file: site_meta.zip
    - Unzip
    - Open:

        *site_meta.xml/meta/system-objecttype-extensions.xml

    - Re-write what we need in order to have the instance not suck for testing
    - Zip everythin back up and upload using:

        *sfcc-ci instance:upload site_meat.zip -i <instance_uri>

"""