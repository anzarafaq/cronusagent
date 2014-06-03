
#  
use strict;use LWP::UserAgent;use HTTP::Request;use HTTP::Headers;
my $objUserAgent = LWP::UserAgent->new;
my $objHeader = HTTP::Headers->new;
#$objHeader->push_header('X-EBAY-API-COMPATIBILITY-LEVEL' => '311');


my $request = '';

my $uripath = "http://localhost:11020/services/agent/action/shutdown";


my $objRequest = HTTP::Request->new("POST", $uripath, $objHeader, $request);   


my $objResponse = $objUserAgent->request($objRequest);
if ($objResponse->is_error)
{
    print ("ERROR \n");
    print $objResponse->status_line;
    #print $objResponse->content();

    print ("\n");
}
else
{
    print $objResponse->content();
    print ("\n");
}

